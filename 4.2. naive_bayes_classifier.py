# load the corpus
import nltk
from nltk.corpus import PlaintextCorpusReader
import os
import random 

source_files_path = r"D:\CCI\fileids_txt_cci"
os.chdir(r"D:\CCI\fileids_txt_cci")
corpora = PlaintextCorpusReader(source_files_path, '.*', encoding = "UTF-8")
corpora_fileids = corpora.fileids() #list of name of the file.


# Training set - test set - uids

random.shuffle(corpora_fileids)
test_uids = corpora_fileids[:220] # rough 20%
dev_uids = corpora_fileids[220:440]
train_uids = corpora_fileids[440:]
#print(len(test_uids))
#print(len(dev_uids))
#print(len(train_uids))


# This code create both a dict with uids and their features and labels. 

source_path = r"D:\CCI\naive_bayes_cci\uid_features_cci.csv" # csv file with uid and its features count

import pandas as pd
os.chdir(r"D:\CCI\naive_bayes_cci")
df_features = pd.read_csv("uid_features_cci.csv")
#display(df)


# the following csv file has uid along with its classification label - 0 or 1. with total number of 1 being 333. and total number of 0 being 759.
df_labels = pd.read_csv("cci_uid_orders_labels.csv")
#display(df_labels)
#df_labels.iloc[3][1] # iloc - index and then columns

test_dict_features_label = dict() # features count plus label status. along with UID
dev_dict_features_label = dict()
train_dict_features_label = dict() # features count plus lable status alogn with UID

train_set = list()
dev_set = list()
test_set = list()

for i, r in df_features.iterrows():
    #print(r[0])
    if r[0] in train_uids:
        #print("in the first condition")
        feature = (r[1], r[2], r[3],r[4], r[5], r[6], r[7])
        label = df_labels.iloc[i][1] # accessing specific label status of that file. 
        list_feature_label = [(feature), (label)]
        train_dict_features_label[r[0]] = list_feature_label
        train_set.append(list_feature_label)
    elif r[0] in dev_uids:
        #print("in the second condition")
        feature = (r[1], r[2], r[3],r[4], r[5], r[6], r[7])
        label = df_labels.iloc[i][1] # accessing specific label status of that file. 
        list_feature_label = [(feature), (label)]
        dev_dict_features_label[r[0]] = list_feature_label
        dev_set.append(list_feature_label)
    elif r[0] in test_uids:
        #print("in the third condition")
        feature = (r[1], r[2], r[3],r[4], r[5], r[6], r[7])
        label = df_labels.iloc[i][1] # accessing specific label status of that file. 
        list_feature_label = [(feature), (label)]
        test_dict_features_label[r[0]] = list_feature_label
        test_set.append(list_feature_label)

#print(len(dev_dict_features_label)) #uid: list(features: count)
#print(len(test_dict_features_label))
#print(len(train_dict_features_label))

# formatting the data to run a classifier on it. 

def dataformat(data):
    d=[]
    for i in data:
        tups,z=i
        l=[]
        stri={}
        for tup in tups:
            s,c=eval(tup)
            s="".join(s)
            stri[s]=c
        d.append((stri,z))
    return d



train_data = dataformat(train_set)
test_data = dataformat(test_set)
dev_data = dataformat(dev_set)


# Run a Naive bayes classifier
classifier = nltk.NaiveBayesClassifier.train(train_data)

#accuracy test on dev data 
accuracy = nltk.classify.accuracy(classifier, dev_data)

# check for most informative features
classifier.show_most_informative_features(3)

print(nltk.classify.accuracy(classifier, test_data))

# accuracy approx 90%
# could not run precision, recall, confusion matrix, f1 score test due to paucity of time. 
# ratio of labels in the original dataset was - (333 for 1 : 759 for 0)





