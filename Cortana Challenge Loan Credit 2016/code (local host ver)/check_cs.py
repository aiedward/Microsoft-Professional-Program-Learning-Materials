# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 11:23:25 2017

@author: Runtong
"""

import pandas as pd
import numpy as np
df = pd.read_csv("C:/Users/Runtong/OneDrive/MPP cortana competition/raw_data.csv", header=0)
cs = df['Credit Score']
print("cs is null: " + str(cs.isnull().sum()))
print("cs not null: " + str(cs.notnull().sum()))
print("is cs 20000 null? " + str(cs[20000]))



# Second Round: Drop all rows that has 1.duplicated Loan ID and 2.NaN CreditScore/AnnualIncome
# df['Credit Score'].isnull() & df['Loan ID'].duplicated(keep='last') checks the combined condition while returning the boolean array
df.dropna(axis=0, inplace=True)
df = df[(df['Credit Score'].isnull() & df['Loan ID'].duplicated(keep='last'))==False] # dropped 5249, left 99989


print("\ndataframe length after 2 rounds removal: " + str(len(df))) # 93330
print("unique ID length after 2 rounds removal: " + str(len(df['Loan ID'].unique()))) # 88908    

#third round: Current Loan Amount Wrongly typed as 99999999
#third round cont'd: Credit Score is in range 0-800, those few thousand values should be divided by 10
df = df[(df['Current Loan Amount']!=99999999)] # removed 12378, remaining 80592
df['Credit Score'] = df['Credit Score'].apply(lambda x: x if x <= 1000 else x/10)

print("\nCredit Score max is " + str(df['Credit Score'].max()))  
print("\ndataframe length after 3 rounds removal: " + str(len(df))) # 80592
print("unique ID length after 3 rounds removal: " + str(len(df['Loan ID'].unique()))) # 80592

df.to_csv("C:/Users/Runtong/OneDrive/MPP cortana competition/data_removed_duplicates.csv")