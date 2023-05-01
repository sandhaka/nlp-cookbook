Text Classification: Training Data
---
Training data for NLP projects comes in many different formats. 
For some common formats such as CoNLL, spaCy provides converters you can use from the command line. 
In other cases you’ll have to prepare the training data yourself.

- [x] Example 1: [enron/setup.py](./enron/setup.py) extract training data from Enron dataset and assign a category interactively to each entry.
- [x] Example 2: [bbc/setup.py](./bbc/setup.py) just prepare the training data in the preprocess.py expected format.
- [x] [preprocess.py](./preprocess.py) prepare data and creates training and validation sets (*Automated* by spacy project).

#### Examples
##### Enron Dataset
Interactively prepare dataset from [Enron](https://www.kaggle.com/datasets/wcukierski/enron-email-dataset) db samples.
Arguments are categories and output path. The *.json file contains a list of [SetElement](./set_element.py) elements. Text with assigned labels. 
```shell
python -m ./enron/setup.py nobusiness business ./data.train.json
python -m ./enron/setup.py nobusiness business ./data.eval.json
```
##### BBC Dataset
BBC Dataset categories are in place. Don't need manual assignment
```shell
python -m ./bbc/setup.py ./data.train.json ./data.eval.json
```