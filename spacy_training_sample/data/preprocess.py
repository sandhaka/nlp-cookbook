import pandas as pd
import re
import spacy

# Extracting data from emails
data = pd.read_csv("split_emails.csv", sep=",", quotechar='"')
emails = []
for index, row in data.iterrows():
    message = row[2]
    from_match = re.search("From:.*", message)
    to_match = re.search("To:.*", message)
    sub_match = re.search("Subject:.*", message)
    body = re.findall("^(?!.*\n){0,15}(.|\n)*?(.*)", message, re.MULTILINE)
    e = (
        int(row[0]),
        message[from_match.start() + 5 : from_match.end()].strip() if from_match is not None else None,
        message[to_match.start() + 3 : to_match.end()].strip() if to_match is not None else None,
        message[sub_match.start() + 8 : sub_match.end()].strip() if sub_match is not None else None,
        "".join(map(lambda x: x[1], body[15:])),
    )
    emails.append(e)

# Prepare set
# nlp = spacy.blank("en_core_web_lg")
# data_tuples = ((em[4], em) for em in emails)
# for doc, tpl in nlp.pipe(data_tuples, as_tuples=True):
