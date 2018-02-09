#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
import numpy as np
from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

clf1 = NearestCentroid()
clf1.fit(features_train, labels_train)
#NearestCentroid(metric='euclidean', shrink_threshold=None)
pred = clf1.predict(features_test)

acc = accuracy_score(pred, labels_test)

print("Nearest centroids:", acc)

clf2 = RandomForestClassifier()

clf2.fit(features_train, labels_train)

pred2 = clf2.predict(features_test)

acc2 = accuracy_score(pred2, labels_test)

print("Random forest:", acc2)

clf = AdaBoostClassifier(n_estimators=100)

clf.fit(features_train, labels_train)

pred3 = clf.predict(features_test)

acc3 = accuracy_score(pred3, labels_test)

print("Adaboost:", acc3)

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
