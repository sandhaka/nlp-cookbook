Text Classification: Training Data
---
Training data for NLP projects comes in many different formats. 
For some common formats such as CoNLL, spaCy provides converters you can use from the command line. 
In other cases you’ll have to prepare the training data yourself. 
In our scenario we start from a csv [file](split_emails.csv).

- [enron_dataset_setup.py](./enron_dataset_setup.py) extract training data from Enron dataset and assign a category interactively to each entry.
- [preprocess.py](./preprocess.py) prepare data and creates training and validation sets.

#### Examples
Interactively prepare dataset from [Enron](https://www.kaggle.com/datasets/wcukierski/enron-email-dataset) db samples.
Arguments are categories and output path. The *.json file contains a list of [SetElement](./set_element.py) elements. Text with assigned labels. 
```shell
python -m enron_dataset_setup.py nobusiness business ./labelleddata.train.json
python -m enron_dataset_setup.py nobusiness business ./labelleddata.eval.json
```

> The following should be automated by spacy project command:
```shell
python -m preprocess.py ./labelleddata.train.json ./train.spacy
python -m preprocess.py ./labelleddata.eval.json ./eval.spacy
```