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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print("number of data points: %r" % len(enron_data))
print("number of features: %r" % len(enron_data["SKILLING JEFFREY K"]))

POI = 0
for i in enron_data:
	if (enron_data[i]["poi"] == 1):
		POI+=1

print("number of POIs: %r" % POI)
print("total value of the stock belonging to James Prentice: %r" % enron_data["PRENTICE JAMES"]["total_stock_value"])
print("email messages from Wesley Colwell to persons of interest: %r" % enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
print("value of stock options exercised by Jeffrey Skilling: %r" % enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])
max_money = max(enron_data["SKILLING JEFFREY K"]["total_payments"], enron_data["LAY KENNETH L"]["total_payments"], enron_data["FASTOW ANDREW S"]["total_payments"])
print("the one who took the most money: %r" % max_money)

salary = 0
email = 0
for i in enron_data:
	if (enron_data[i]["salary"] != "NaN"):
		salary += 1
	if (enron_data[i]["email_address"] != "NaN"):
		email += 1

print("folks that have a quantified salary: %r" % salary)
print("folks that have a quantified email: %r" % email)
