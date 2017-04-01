# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 00:18:14 2017

@author: Runtong
"""

import pandas as pd
import numpy as np
from sklearn import preprocessing
df = pd.read_csv("C:/Users/Runtong/OneDrive/MPP cortana competition/data_removed_duplicates_Updated.csv",header=0)

df['Loan Status'] = df['Loan Status'].map({'Charged Off':1, 'Fully Paid':0})
df['Term'] = df['Term'].astype("category").cat.codes
df['Credit Score'] = pd.DataFrame(np.log(df['Credit Score'].as_matrix()))
df['Annual Income'] = df['Annual Income'].clip(upper=250000)
df['Monthly Debt'] = df['Monthly Debt'].clip(upper=4000)
df['Years of Credit History'] = df['Years of Credit History'].clip(upper=40)
df['Number of Open Accounts'] = df['Number of Open Accounts'].clip(upper=25)
df['Number of Credit Problems'] = df['Number of Credit Problems'].apply(lambda x: x if x==0  else 1)  
df['Current Credit Balance'] = df['Current Credit Balance'].clip(upper=80000)
df['Maximum Open Credit'] = df['Maximum Open Credit'].clip(upper=100000)  
df['Bankruptcies'] = df['Bankruptcies'].apply(lambda x: x if x==0  else 1)  
df['Tax Liens'] = df['Tax Liens'].apply(lambda x: x if x==0  else 1) 
  
  
# preprocessing in batch
list = ['Current Loan Amount', 'Annual Income', 'Credit Score','Monthly Debt','Years of Credit History','Number of Open Accounts','Current Credit Balance','Maximum Open Credit']
for items in list:
    df[items] = preprocessing.StandardScaler().fit_transform(df[items])
