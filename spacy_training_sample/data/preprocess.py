import json
import spacy
import typer

from pathlib import Path
from spacy.tokens import DocBin

from spacy_training_sample.data.set_element import SetElement, SetElementDecoder


def main(
    input_path: Path = typer.Argument(..., exists=True, dir_okay=False),
    output_path: Path = typer.Argument(..., dir_okay=False),
):
    docs = DocBin()
    with open(input_path, "r") as f:
        data: list[SetElement] = json.load(f, cls=SetElementDecoder)
    nlp = spacy.blank("en")
    for doc, item in nlp.pipe([(el.text, el) for el in data], as_tuples=True):
        for cat in item.categories:
            doc.cats[cat] = item.categories[cat]
        docs.add(doc)
    docs.to_disk(output_path)


if __name__ == "__main__":
    typer.run(main)
