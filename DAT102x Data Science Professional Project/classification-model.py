# -*- coding: utf-8 -*-
"""
Created on Sun Apr 09 11:33:45 2017

@author: Runtong
"""

import pandas as pd
train_path = "C:/Users/Runtong/OneDrive/MPP capstone project 2017/AWCustomers/Classificationtrain-data-processed.csv"
test_path = "C:/Users/Runtong/OneDrive/MPP capstone project 2017/AWCustomers/Classificationtest-data-processed.csv"
test_ID_path = "C:/Users/Runtong/OneDrive/MPP capstone project 2017/AWCustomers/AWTest-Classification.csv"

def encoding(df):
    # data wrangling: encoding categorical/string values
    from sklearn import preprocessing
    string_val_list = [
            'Education',
            'Occupation',
            'Gender',
            'MaritalStatus'
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

# train classification model
y = train_df['BikeBuyer'].copy()
X = train_df.drop(labels=['BikeBuyer'], axis=1)
from sklearn import cross_validation
data_train, data_test, label_train, label_test = cross_validation.train_test_split(X, y, test_size=0.33, random_state=1)

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(max_depth=8, random_state=1)
clf.fit(X,y)
predict_decisionTree = pd.DataFrame({"CustomerID":CustomerID,"label":clf.predict(test_df),"score":clf.predict_proba(test_df)[:,1]})

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(max_depth=8, random_state=1)
clf.fit(X,y)
predict_decisionForest = pd.DataFrame({"CustomerID":CustomerID,"Forest_label":clf.predict(test_df),"Forest_score":clf.predict_proba(test_df)[:,1]})

joined_label = predict_decisionTree.set_index('CustomerID').join(predict_decisionForest.set_index('CustomerID'))
joined_label['agree'] = 1*(joined_label.label==joined_label.Forest_label)