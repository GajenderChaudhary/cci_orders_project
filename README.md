# cci_orders_project

This project does text classification of the orders passed by the Competition Commission of India from 2010 to 2021.  

It has four major coding stages.

First, Reorganizing the CCI orders in the system and creating a Unique ID for each of them that retains the metadata of the file such as year in which it is passed and further subcategories. 

In the second stage, I did OCR of the pdf files in two process. First, converting the pdf files into img files and then extracting text from those files. 
(Note - Python Libraries such as Pypdf2 and Textract, were not able to extract text from some of the pdf, thats why OCR decision was taken)

Third, Once the files are converted into txt files, Using NLTK and pandas library, exploratory phase began. 

In the fourth stage, Naive bayes classifier was trained and tested. 
(#could not run precision, recall, confusion matrix, F1 score due to paucity of time.)
