import nltk 
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.util import ngrams
import os
import pandas as pd


# Whole Feature Extraction Code
#predefined Bag of words in the list, txt_bigram, txt_trigram.
# this code reads the text file and reture a dictionary count for each item in the bag of words. 


def feature_extractor(text_file, source_location):
    os.chdir(source_location)
    fh = open(text_file, "r", encoding = 'utf-8')
    txt = fh.read()
    txt = txt.lower()
    fh.close()
    txt_unigram_lemma = ["closed", "closure",  "close"]# treat it as one lemma
    txt_bigram = [("no", "violation"), ("section", "27")] 
    txt_trigram = [('section', '26', '2'),('section', '26', "1"), ('section', '26','6'), ("no", "prima", "facie")]
    feature_count = {"close" : 0, ("no", "violation"): 0, ("section", "27"): 0, ('section', '26', '2'): 0, ('section', '26', "1"): 0, ('section', '26','6'):0, ("no", "prima", "facie"):0}
    tokens = [w for w in nltk.word_tokenize(txt) if w not in list(punctuation)]
    close = [w for w in tokens if w in txt_unigram_lemma] # I am treating close as a lemma
    bigram = [w for w in nltk.ngrams(tokens, 2) if w in txt_bigram]
    trigram = [w for w in nltk.ngrams(tokens, 3) if w in txt_trigram]
    feature_count["close"] = len(close)
    feature_count[("no", "violation")] = bigram.count(("no", "violation")) 
    feature_count[("section", "27")] = bigram.count(("section", "27")) # list count method 
    feature_count[('section', '26', '2')] = trigram.count(('section', '26', '2'))
    feature_count[('section', '26', "1")] = trigram.count(('section', '26', '1'))
    feature_count[('section', '26','6')] = trigram.count(('section', '26','6'))
    feature_count[("no", "prima", "facie")] = trigram.count(("no", "prima", "facie")) 
    return feature_count


def dict_to_list_of_tuple(dictionary):
    list_of_tuples = list()
    for k, v in feature_dict.items():
        tup = (k, v)
        list_of_tuples.append(tup)
    return list_of_tuples

def dict_to_csv(dictionary):
    import pandas as pd
    df = pd.DataFrame.from_dict(dictionary, orient ="columns")
    df = df.T
    os.chdir("D:\CCI\naive_bayes_cci")
    df.to_csv("uid_features_cci.csv")
    

uid_feature_dict = dict()
for ids in corpora_fileids:
    print(ids)
    feature_dict = feature_extractor(ids,r"D:\CCI\fileids_txt_cci") # extracting features count from the text file
    list_of_tuple = dict_to_list_of_tuple(feature_dict)
    uid_feature_dict[ids] = list_of_tuple

# saved that extracted feature into a csv file.
dict_to_csv(uid_feature_dict)



