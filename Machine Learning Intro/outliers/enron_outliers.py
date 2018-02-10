#!/usr/bin/python

import pickle
import numpy as np
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb"), fix_imports=True)

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

#print(data)
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


data_dict.pop('TOTAL', 0)
print(data_dict["METTS MARK"])
# To Find outlier
for key, value in data_dict.items():
    if(value['bonus'] == "NaN"):
        continue
    if int(value['bonus']) > 1000000:
        print("{} {}".format(key, value['bonus']))
        
