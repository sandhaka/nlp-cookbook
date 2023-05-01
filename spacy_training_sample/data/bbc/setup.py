import math
import pandas as pd
import json
import typer

from pathlib import Path

from spacy_training_sample.data.set_element import SetElement, SetElementEncoder


def main(
    output_train_path: Path = typer.Argument(..., dir_okay=False),
    output_eval_path: Path = typer.Argument(..., dir_okay=False),
):
    train_set = []
    eval_set = []
    categories = ["sport", "business", "politics", "tech", "entertainment"]
    data = pd.read_csv("bbc-text.csv", sep=",", quotechar='"')
    set_size = math.floor(len(data) / 2)
    for index, row in data.iterrows():
        cat = row[0]
        text = row[1]
        cats = dict(map(lambda c: (c, False), categories))
        cats[cat] = True
        # noinspection PyTypeChecker
        if index < set_size:
            train_set.append(SetElement(index, text, cats))
        else:
            eval_set.append(SetElement(index, text, cats))
    with open(output_train_path, "w", newline="") as f:
        json.dump(train_set, f, sort_keys=True, cls=SetElementEncoder)
    with open(output_eval_path, "w", newline="") as f:
        json.dump(eval_set, f, sort_keys=True, cls=SetElementEncoder)


if __name__ == "__main__":
    typer.run(main)
