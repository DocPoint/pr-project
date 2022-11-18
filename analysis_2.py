# -*- coding: utf-8 -*-
"""Analysis_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ik62qq5P9yIaiXg4kKq-30om6HnMlrrN
"""

#Importing Libraries 

import pandas as pd
import numpy as np
import re          #regular expression
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.simplefilter("ignore")
data = pd.read_csv("Language Detection.csv")
data.head(10)

data["Language"].value_counts() #value_counts() is used to get a Series containing counts of unique values.

#Separating Independent and Dependent features
X = data["Text"]
y = data["Language"]

#Label Encoding to convert it into a numerical form
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

data_list = []

# iterating through all the text
for text in X:         
    text = re.sub(r'[!@#$(),n"%^*?:;~`0-9]', ' ', text)      # removing the symbols and numbers
    text = re.sub(r'[[]]', ' ', text)   
    text = text.lower()          # converting the text to lower case
    data_list.append(text)       # appending to data_list
#Bag of Words [ converting text into numerical form by creating a Bag of Words model using CountVectorizer.]
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer() # tokenize a collection of text documents
X = cv.fit_transform(data_list).toarray()
X.shape # (10337, 39419)

#train-test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=42)
# Model Training
from sklearn.naive_bayes import MultinomialNB  #classifier is suitable for classification with discrete features
model = MultinomialNB()
model.fit(x_train, y_train)

#predict output for test dataset
y_pred = model.predict(x_test)
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
ac = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
print("Accuracy is :",ac)

#Predicting with some more data

def predict(text):
     x = cv.transform([text]).toarray() # converting text to bag of words model (Vector)
     lang = model.predict(x) # predicting the language
     lang = le.inverse_transform(lang) # finding the language corresponding the the predicted value
     print("The langauge is in",lang[0]) # printing the language

predict('People are awesome Hi there')

predict('നൽകുന്നു')

predict('hi')

predict('வணக்கம்')

predict('hallo')

predict('तुम एक अद्भुत हो')

predict('Ruchi fik 18 point')

predict('ouais eu les résultats')

predict('hlw')