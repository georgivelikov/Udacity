#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
import numpy as np
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

original = '../tools/python2_lesson14_keys.pkl'
destination = '../tools/python2_lesson14_keys_unix.pkl'

content = ''
outsize = 0
with open(original, 'rb') as infile:
    content = infile.read()
with open(destination, 'wb') as output:
    for line in content.splitlines():
        outsize += len(line) + 1
        output.write(line + str.encode('\n'))
        
data = featureFormat(data_dict, features_list, sort_keys = destination)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()

clf.fit(features, labels)

print(clf.score(features, labels))

from sklearn.cross_validation import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier()

clf.fit(features_train, labels_train)

print(clf.score(features_test, labels_test))

all_test_poi_count = np.count_nonzero(labels_test)
print(all_test_poi_count)

all_test_people = len(labels_test)
print(all_test_people)
predict = clf.predict(features_test)
for i in range(1, all_test_people):
    print("{} {} {}".format(i, predict[i], labels_test[i]))

from sklearn import metrics

print(metrics.precision_score(labels_test, predict)) 
print(metrics.recall_score(labels_test, predict)) 



