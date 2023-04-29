Text Classification: Configuration
---
Create a pipeline configuration to run our sample session
### Cli
Run the `init config` command and specify your requirements and settings.

##### Pipeline components:
- [`Tok2Vec`](https://spacy.io/api/tok2vec): map each token into a vector representation.
- `textcat`: is a [TextCategorizer](https://spacy.io/api/textcategorizer) step.
##### Language:
English
##### Optimization:
Accuracy
```shell
python -m spacy init config --lang en --pipeline tok2vec,textcat_multilabel --optimize accuracy sample.config.cfg
```
The configuration has been saved to [sample.config.cfg](sample.config.cfg) file