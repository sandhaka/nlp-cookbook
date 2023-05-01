import pandas as pd
import re
import json
import typer

from random import shuffle
from pathlib import Path
from collections import deque

from spacy_training_sample.data.set_element import SetElement, SetElementEncoder


def main(
    labels: list[str] = typer.Argument(...),
    output_path: Path = typer.Argument(..., dir_okay=False),
):
    # Extracting data from emails
    data = pd.read_csv("10k_enron_dataset.csv", sep=",", quotechar='"')
    items = []

    def is_inbox(text):
        return re.match(".*inbox.*", text, re.IGNORECASE) is not None

    def is_from_enron(text):
        return re.match(".*@enron.com.*", text, re.IGNORECASE) is not None

    def extract_body(msg):
        lines = msg.split("\n")
        lines.reverse()
        b = ""
        q = deque(lines)
        while q:
            line = q.pop()
            if line != "":
                continue
            while q:
                next_line = q.pop()
                if re.match(".*-----Original Message-----.*", next_line) is not None:  # Ignore attached messages
                    return b
                if re.match(".*--- Forwarded by.*", next_line) is not None:  # Ignore forwarding info
                    return b
                b += next_line + "\n"
        return b

    for index, row in data.iterrows():
        message = row[2]
        folder_match = re.search("X-Folder:.*", message)
        from_match = re.search("From:.*", message)

        folder_name = message[folder_match.start() + 9 : folder_match.end()].strip()
        from_address = message[from_match.start() + 5 : from_match.end()].strip()
        print(extract_body(message))
        # Consider only inbox email
        if is_inbox(folder_name) and is_from_enron(from_address):
            to_match = re.search("To:.*", message)
            sub_match = re.search("Subject:.*", message)
            to_address = message[to_match.start() + 3 : to_match.end()].strip()
            subject = message[sub_match.start() + 8 : sub_match.end()].strip()
            body = extract_body(message)
            e = (int(row[0]), from_address, to_address, subject, body, dict([(i, False) for i in labels]))
            i = SetElement(e[0], e[4], e[5])
            items.append(i)

    # Prepare set interactively
    shuffle(items)

    print(
        "Type 'terminate' to end the labelling.\n"
        "The remaining texts will be ignored and the "
        "labelled ones will be used as training and validation sets.\n"
        "WARN: Subject content are not used in training\n"
    )

    print(f"Categories: {labels}")

    labelled_items = []
    for item in items:
        for cat in labels:
            item.categories[cat] = False
        print("")
        print(item.text)
        while True:
            typed = input(
                f"(press [q|terminate] to end labelling or exit and ignore remains texts).\n"
                f"Enter the category from {labels}: "
            )
            if typed in ["q", "terminate"]:
                break
            elif typed not in labels:
                print(f"Unknown label: {typed}")
            else:
                item.categories[typed] = True
        if typed == "terminate":
            break
        else:
            labelled_items.append(item)

    with open(output_path, "w", newline="") as f:
        json.dump(labelled_items, f, sort_keys=True, cls=SetElementEncoder)


if __name__ == "__main__":
    typer.run(main)
