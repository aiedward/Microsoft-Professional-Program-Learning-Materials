# python 2.7
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 10:28:01 2017

@author: Runtong
"""

import pandas as pd
customer_path = "C:/Users/Runtong/OneDrive/MPP capstone project 2017/AWCustomers/AWCustomers.csv"
sales_path = "C:/Users/Runtong/OneDrive/MPP capstone project 2017/AWCustomers/AWSales.csv"
customer = pd.read_csv(customer_path)
sales = pd.read_csv(sales_path)


# drop those columns not helpful for both of the tasks
drop_list = [
        "Title",
        "FirstName",
        "MiddleName",
        "LastName",
        "Suffix",
        "AddressLine1",
        "AddressLine2",
        "PostalCode",
        "PhoneNumber",
        "LastUpdated"
        ]
customer.drop(axis=1, labels=drop_list, inplace=True)
customer.drop_duplicates(inplace=True)
customer.reset_index(drop=True, inplace=True)
print "remaining entries: ", len(customer)
print "\n----------\n"

# drop duplicates
# look at what are the duplicates
customer[customer['CustomerID'].duplicated(keep=False)].CustomerID
## [out]:
#834    13385 - different YearlyIncome
#947    24334 - different Matial Status

# since only 2 data points does not affect the whole picture, drop them all.
customer.drop(customer.index[[834, 835, 947, 948]], inplace=True)
customer.reset_index(drop=True, inplace=True)

# now all entries should be unique
print"number of data point: ", len(customer)
print"number of unique CustomerID: ", customer.CustomerID.nunique()
print"\n--------------\nend of preprocessing"
