#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
import numpy as np
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
cls = SVC(kernel="rbf", C=10000)

#features_train = features_train[:int(len(features_train)/100)] 
#labels_train = labels_train[:int(len(labels_train)/100)] 

t0 = time()
cls.fit(features_train, labels_train)
print("training time:", round(time()-t0, 3), "s")

t0 = time()
pred = cls.predict(features_test)
print("prediction time:", round(time()-t0, 3), "s")

acc = accuracy_score(pred, labels_test)
print(acc)

print(pred[10])
print(pred[26])
print(pred[50])

print(np.count_nonzero(pred))
#########################################################
### your code goes here ###

#########################################################


