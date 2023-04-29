Text Classification: Training Data
---
Training data for NLP projects comes in many different formats. 
For some common formats such as CoNLL, spaCy provides converters you can use from the command line. 
In other cases you’ll have to prepare the training data yourself. 
In our scenario we start from a csv [file](split_emails.csv).

With [preprocess.py](setup.py) setups data and creates training and validation sets.