# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Importing the dataset
dataset = pd.read_csv("Social_Network_Ads.csv")
#Converting Gender Column into numbers
dataset.loc[dataset["Gender"] == "Male", "Gender"] = 1
dataset.loc[dataset["Gender"] == "Female", "Gender"] = 0
#Removing Columns
X = dataset.iloc[:, [2, 3, 4]].values
y = dataset.iloc[:, -1].values
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
# Training the Naive Bayes model on the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)
# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred2 = classifier.predict(X_train)
# Making the Confusion Matrix 
from sklearn.metrics import confusion_matrix, accuracy_score
ac = accuracy_score(y_test,y_pred)
cm = confusion_matrix(y_test, y_pred)
ac_train = accuracy_score(y_train,y_pred2)
print(cm,ac,ac_train)
