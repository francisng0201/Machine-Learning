#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm 

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
#clf = svm.SVC(kernel = "rbf", C = 10)
#clf.fit(features_train, labels_train)
#print(clf.score(features_test, labels_test))
#clf = svm.SVC(kernel = "rbf", C = 100)
#clf.fit(features_train, labels_train)
#print(clf.score(features_test, labels_test))
#clf = svm.SVC(kernel = "rbf", C = 1000)
#clf.fit(features_train, labels_train)
#print(clf.score(features_test, labels_test))
clf = svm.SVC(kernel = "rbf", C = 10000)
clf.fit(features_train, labels_train)
print(clf.score(features_test, labels_test))

pred = clf.predict(features_test)
print("10th: %r, 26th: %r, 50th: %r" % (pred[10], pred[26], pred[50]))
print("in Chris: %r" % sum(pred))
#########################################################


