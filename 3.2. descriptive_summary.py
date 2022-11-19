import nltk
import pandas as pd
import os
from nltk.util import ngrams
from nltk import word_tokenize
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from string import punctuation


# Functions

def Bag_of_words(text):# could have used ngram as unigram but wanted to remove stopwords, punctuation
    text = str(text)
    tokens = nltk.word_tokenize(text.lower())# lowercase words. 
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if not w.lower() in stop_words and w not in list(punctuation) ] # remove punctuation and stopwords
    bag_of_words = dict()
    for i in filtered_tokens:
        bag_of_words[i] = bag_of_words.get(i, 0) + 1
    return filtered_tokens, bag_of_words


# Ngram function takes two arguments - returns two variables one list of all ngrams, and dict count
def ngram(text, n): 
    text = str(text) # to avoid float arguments
    tokens = nltk.word_tokenize(text.lower())
    token_ngram = list(nltk.ngrams(tokens, n))
    ngram_dict = {}
    for i in token_ngram:
        ngram_dict[i] = ngram_dict.get(i, 0) + 1
    return token_ngram, ngram_dict
  
  
source_file_path = "D:\CCI\sorted_cci_year_orders_txt.csv"
os.chdir("D:\CCI")
cci_orders = pd.read_csv("sorted_cci_year_orders_txt.csv")
cci_orders
  

# Added new columns
columns_name = ["filtered_tokens","filtered_bag_of_words", "bigrams", "bigrams_count", "trigrams", "trigram_count"]
for i in columns_name:
    cci_orders[i] = ""
cci_orders


# to remove first column
cci_orders = cci_orders.drop(cci_orders.columns[0], axis =1)
cci_orders


# to fill in the values
for index, row in cci_orders.iterrows():
    text = row["Text"]
    filtered_words = list(Bag_of_words(text)) # pass in the text to the function - at index 0 - list of filtered tokens, at index 1 count of those tokens.
    tokens = filtered_words[0]
    bow = filtered_words[1]
    bigram = list(ngram(text, 2)) # Function above - return at index 0 list of bigrams, at index 1, the count of bigrams
    trigram = list(ngram(text, 3)) # function above - return at index 0 list of trigrams, at index 1, the count of trigrams
    cci_orders.at[index, columns_name[0]] = tokens 
    cci_orders.at[index, columns_name[1]] = bow
    cci_orders.at[index, columns_name[2]] = bigram[0]
    cci_orders.at[index, columns_name[3]] = bigram[1]
    cci_orders.at[index, columns_name[4]] = trigram[0]
    cci_orders.at[index, columns_name[5]] = trigram[1]   
display(cci_orders)



# Extracting the csv file

os.chdir("D:\CCI\Text_statistics")
cci_orders.to_csv("bow_ngrams_cci_orders_per_page.csv")






  
