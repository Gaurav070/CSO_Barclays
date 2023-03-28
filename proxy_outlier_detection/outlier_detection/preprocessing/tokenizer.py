import string
import spacy
spacy.load("en_core_web_sm")
from spacy.lang.en import English
#spacy.load('en')
parser = English()
# tokenizing the raw text
def tokenizeText(sample):
    clean_sample = sample.replace("/", "").replace(";","").replace("(","").replace(")", "").replace("-","").replace(",", "")
    tokens = parser(clean_sample).to_bytes()
    
    
    # lemmatization
#     lemmas = []
#     for tok in tokens:
#         lemmas.append(tok)
#     tokens = lemmas
#     print(tokens)
    # remove stop words and special characters
    #tokens = [tok for tok in tokens if tok.lower() not in STOPLIST]
    #tokens = [tok.replace("/", "").replace(";","").replace("(","").replace(")", "") for tok in tokens]
    
# #     # only take words with length greater than or equal to 3
# #     tokens = [tok for tok in tokens if len(tok) >= 3]
    
    # remove remaining tokens that are not alphabetic
    #tokens = [tok for tok in tokens if tok.is_alpha_num]
    
#     # stemming of words
#     porter = PorterStemmer()
#     tokens = [porter.stem(word) for word in tokens]
    
    return list(tokens)