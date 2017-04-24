# -*- coding: utf-8 -*-
"""
Created on Sun Apr 09 17:06:50 2017

@author: Runtong
"""

import pandas as pd
train_path = "C:/Users/Runtong/OneDrive/MPP capstone project 2017/AWCustomers/Regressiontrain-data-processed.csv"
test_path = "C:/Users/Runtong/OneDrive/MPP capstone project 2017/AWCustomers/Regressiontest-data-processed.csv"
test_ID_path = "C:/Users/Runtong/OneDrive/MPP capstone project 2017/AWCustomers/AWTest-Regression.csv"

def encoding(df):
    # data wrangling: encoding categorical/string values
    from sklearn import preprocessing
    string_val_list = [
            'Occupation',
            'Gender',
            'MaritalStatus',
            'CountryRegionName'
            ]
    for items in string_val_list:
        le = preprocessing.LabelEncoder()
        le.fit(df[items].unique())
        df[items] = le.transform(df[items])              
    return df

train_df = encoding(pd.read_csv(train_path, index_col=0))
test_df = encoding(pd.read_csv(test_path, index_col=0))
CustomerID = pd.read_csv(test_ID_path).CustomerID

print train_df.dtypes
print test_df.dtypes

import numpy as np
train_df.YearlyIncome = np.log(train_df.YearlyIncome)
test_df.YearlyIncome = np.log(test_df.YearlyIncome)

# train classification model
y = train_df['AvgMonthSpend'].copy()
X = train_df.drop(labels=['AvgMonthSpend'], axis=1)
from sklearn import cross_validation
data_train, data_test, label_train, label_test = cross_validation.train_test_split(X, y, test_size=0.33, random_state=1)

from sklearn.tree import DecisionTreeRegressor
model = DecisionTreeRegressor(max_depth=8, random_state=1)
model.fit(X,y)
predict_decisionTree = pd.DataFrame({"CustomerID":CustomerID,"predict-tree":model.predict(test_df)})

from sklearn import linear_model
model = linear_model.LinearRegression()
model.fit(X,y)
predict_decisionForest = pd.DataFrame({"CustomerID":CustomerID,"predict-linear":model.predict(test_df)})

joined_label = predict_decisionTree.set_index('CustomerID').join(predict_decisionForest.set_index('CustomerID'))
joined_label['diff'] = joined_label['predict-tree'] - joined_label['predict-linear']
joined_label['avg'] = (joined_label['predict-tree'] + joined_label['predict-linear'])/2
