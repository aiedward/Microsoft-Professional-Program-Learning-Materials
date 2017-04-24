# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 10:47:31 2017

@author: Runtong
"""

# Classification Model Data Transformation
import pandas as pd
train_path = "C:/Users/Runtong/OneDrive/MPP capstone project 2017/AWCustomers/AWJoined_after_wrangling.csv"
df = pd.read_csv(train_path, index_col=0)
# data wrangling: convert datatypes, and make categorical
cateogrical_val_list = [
        'City',
        'StateProvinceName',
        'CountryRegionName',
        'Education',
        'Occupation',
        'Gender',
        'MaritalStatus',
        'HomeOwnerFlag',
        'NumberCarsOwned',
        'NumberChildrenAtHome', 
        'TotalChildren',
        'age',
        'year',
        'month',
        'day', 
        ]
for items in cateogrical_val_list:
    df[items] = df[items].astype('category')

# Drop BirthDate, year, month, day
df.drop(axis=1, labels=['BirthDate','year','month','day'], inplace=True)
# Drop AvgMonthSpend: not within scope of experiment
df.drop(axis=1, labels=['AvgMonthSpend'], inplace=True)

# YearlyIncome natural log scale
import numpy as np
df.YearlyIncome = np.log(df.YearlyIncome)

# give a clue how AvgMonthSpend vs. YearlyIncome
# scatter_matrix would not take the categorical arguments
def scatter_matrix_PLOT(df):
    import matplotlib.pyplot as plt
    from pandas.tools.plotting import scatter_matrix
    fig = plt.figure(figsize=(10, 10))
    fig.clf()
    ax = fig.gca()
    scatter_matrix(df, alpha=0.3, 
                   diagonal='kde', ax = ax)
    return 'Done'
scatter_matrix_PLOT(df.sample(n=400))

# remove non-influential parameters
df.drop(axis=1, labels=['City','StateProvinceName','CountryRegionName'], inplace=True)
    
print df.describe()
print "\n\n"
print df.dtypes

from data-processing-function import test_data_processing
test_path = "C:/Users/Runtong/OneDrive/MPP capstone project 2017/AWCustomers/AWTest-Classification.csv"
test = pd.read_csv(test_path)
test_processed = test_data_processing(test)
test_processed.to_csv("Classificationtest-data-processed.csv")
df.to_csv("Classificationtrain-data-processed.csv")