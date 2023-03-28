import spacy
spacy.load("en_core_web_sm")
from spacy.lang.en import English
#spacy.load('en')
parser = English()
# tokenizing the raw text
def tokenizeText(sample):
    clean_sample = sample.replace("/", "").replace(";","").replace("(","").replace(")", "").replace("-","").replace(",", "")
    tokens = parser(clean_sample).to_bytes()
    return list(tokens)