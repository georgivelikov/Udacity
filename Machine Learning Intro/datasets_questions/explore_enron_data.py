#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
import pickle

original = "../final_project/final_project_dataset.pkl"
destination = "../final_project/final_project_dataset_unix.pkl"

content = ''
outsize = 0
with open(original, 'rb') as infile:
    content = infile.read()
with open(destination, 'wb') as output:
    for line in content.splitlines():
        outsize += len(line) + 1
        output.write(line + str.encode('\n'))
        
enron_data = pickle.load((open(destination, "rb")),fix_imports=True)

print(enron_data["SKILLING JEFFREY K"]["bonus"])

print(len(enron_data))

print(len(enron_data["SKILLING JEFFREY K"]))

poi_count = 0
for participant in enron_data:
    if(enron_data[participant]["poi"] == 1):
        poi_count += 1
print(poi_count)

print(enron_data["SKILLING JEFFREY K"].keys())
print(enron_data.keys())

print(enron_data["PRENTICE JAMES"]["total_stock_value"])

print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

print(enron_data["SKILLING JEFFREY K"]["total_payments"])

print(enron_data["LAY KENNETH L"]["total_payments"])

print(enron_data["FASTOW ANDREW S"]["total_payments"])

print(enron_data["FASTOW ANDREW S"]["shared_receipt_with_poi"])

salary_count = 0
email_count = 0
for participan in enron_data:
    if(enron_data[participan]["salary"] != "NaN"):
        salary_count += 1
    if(enron_data[participan]["email_address"] != "NaN"):
        email_count += 1
print(salary_count)        
print(email_count)

total_payments_count = 0
for participan in enron_data:
    if(enron_data[participan]["total_payments"] == "NaN"):
        total_payments_count += 1  
    
print(total_payments_count)
print(total_payments_count / 146) 

total_payments_count_poi = 0
for participan in enron_data:
    if(enron_data[participan]["poi"] == 1):
        if(enron_data[participan]["total_payments"] == "NaN"):
            total_payments_count_poi += 1  
    
print(total_payments_count_poi)
print(total_payments_count_poi / 146)    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        