import os
import nltk 
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import words
from collections import Counter
from nltk.probability import FreqDist
from nltk import word_tokenize
from nltk.corpus import words
from nltk.corpus import stopwords

# Loading your corpus

source_files_path = "D:\CCI\cci_txt_pytesseract_OCR"
#os.chdir("D:\CCI")
cci_corpora = PlaintextCorpusReader(source_files_path, '.*', encoding = "UTF-8")
cci_fileids = cci_corpora.fileids() #list of name of the file. 


# Generated appended text files of total 1092

source_files_path = "D:\CCI\cci_txt_pytesseract_OCR"
output_path = "D:\CCI\fileids_txt_cci"

for ids in cci_fileids:
    print(ids)
    os.chdir(r"D:\CCI\cci_txt_pytesseract_OCR")
    fh = open(ids, 'r', encoding = "utf-8")
    txt = fh.read()
    fh.close()
    os.chdir(r"D:\CCI\fileids_txt_cci")
    new_str = ids.split("_")
    new_fh = open(f"{new_str[0]}_{new_str[1]}_{new_str[2]}.txt", 'a+', encoding = "utf-8")
    # a+ opens the file if not there, and appends the text to it. 
    new_fh.write(f"\n{txt}\n")
    new_fh.close() 
    
# further compression

source_files_path = r"D:\CCI\fileids_txt_cci"
os.chdir(r"D:\CCI\fileids_txt_cci")
corpora = PlaintextCorpusReader(source_files_path, '.*', encoding = "UTF-8")
corpora_fileids = corpora.fileids() #list of name of the file. 

# generates 12 txt files for each year

source_files_path = r"D:\CCI\fileids_txt_cci"
output_path = r"D:\CCI\year_txt_cci"

for ids in corpora_fileids:
    print(ids)
    os.chdir(r"D:\CCI\fileids_txt_cci")
    fh = open(ids, 'r', encoding = "utf-8")
    txt = fh.read()
    fh.close()
    os.chdir(r"D:\CCI\year_txt_cci")
    new_str = ids.split("_")
    new_fh = open(f"{new_str[0]}.txt", 'a+', encoding = "utf-8")
    new_fh.write(f"\n{txt}\n")
    new_fh.close() 


# generates 1 txt file i.e. an entire corpora.

out_path = r"D:\CCI\entire_cci_corpora"
source_path = r"D:\CCI\year_txt_cci"

os.chdir(r"D:\CCI\year_txt_cci")

entire_corpora = PlaintextCorpusReader(source_path, '.*', encoding = "UTF-8")
entire_corpora = entire_corpora.fileids() #list of name of the file. 


for ids in entire_corpora:
    print(ids)
    os.chdir(r"D:\CCI\year_txt_cci")
    fh = open(ids, 'r', encoding = "utf-8")
    txt = fh.read()
    fh.close()
    os.chdir(r"D:\CCI\entire_cci_corpora")
    new_fh = open("entire_cci_corpora.txt", 'a+', encoding = "utf-8")
    new_fh.write(f"\n{txt}\n")
    new_fh.close() 

    
    
