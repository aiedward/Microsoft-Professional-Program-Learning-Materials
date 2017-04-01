# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 17:40:00 2017

@author: Runtong
"""

import pandas as pd
df = pd.read_csv("C:/Users/Runtong/OneDrive/MPP cortana competition/raw_data.csv", header=0)
# df.head(10)


print("dataframe length at beginning: " + str(len(df))) # 111107
print("unique ID length at beginning: " + str(len(df['Loan ID'].unique()))) # 88910
# Check data type of each attributes, some need conversion
print(df.dtypes)

# Monthly Debt & Maximum Open Credit must be converted to numeric types
# Monthly Debt is having some $ sign
df['Monthly Debt'].replace("\$","",regex=True, inplace=True)
df['Monthly Debt'] = df['Monthly Debt'].astype(float)
# Maximum Open Credit is having 2 "#VALUE" string type values
df = df[(df['Maximum Open Credit']!="#VALUE!")]
df['Maximum Open Credit'] = df['Maximum Open Credit'].astype(float)

# Bankruptcies & Tax Liens & Years of Credit History & Months since last delinquent could be cast to int
# df['Tax Liens'].astype(int)
df['Years of Credit History'] = df['Years of Credit History'].astype(int)
# df['Months since last delinquent'].astype(int)

# Check data type of each attributes again
print("\n")
print(df.dtypes)

# Check duplicates
print("\ndataframe length after type conversion: " + str(len(df))) # 111105
print("unique ID length after type conversion: " + str(len(df['Loan ID'].unique()))) # 88908

# check missing values
df['Credit Score'].isnull().values.ravel().sum() #21337
df['Annual Income'].isnull().values.ravel().sum() #21337

# Missing values are all from ['Credit Score' and 'Annual Income'], and they come in pairs
# if_paired is an all-true array
# A numpy example of array comparison: (np.array([1,1,1,1])&np.array([1,0,0,1])).sum()
if_paired = (df['Credit Score'].isnull() == df['Annual Income'].isnull())
# A detailed check shows that 5249 instances where null values occur accompanying duplicated Loan ID
# and these are values that could be safely deleted.
print((df['Credit Score'].isnull() & df['Loan ID'].duplicated(keep=False)).sum()) # 5249

# First Round: Drop all duplicates
df = df.drop_duplicates(keep='first') # dropped 5869
print("\ndataframe length after dropping all duplicates: " + str(len(df))) # 98579
print("unique ID length after dropping all duplicates: " + str(len(df['Loan ID'].unique()))) # 88908

     
# drop all NaN value from Credit Score (same time Anual Income) 
df = df[df["Credit Score"].notnull()==True]
print("\ndataframe length after dropping all duplicates: " + str(len(df))) # 77242
print("unique ID length after dropping all duplicates: " + str(len(df['Loan ID'].unique()))) # 72820

# Credit Value need to be in range of 0-800
df['Credit Score'] = df['Credit Score'].apply(lambda x: x if x <= 1000 else x/10)

# Current Loan Amount Wrongly typed as 99999999
df = df[(df['Current Loan Amount']!=99999999)] # removed 12378, remaining 80592 

# Years in current job has n/a values
# since stratification show it does not 
# df = df[df['Years in current job']!='n/a']

# Final Check
print("\ndataframe length after dropping all duplicates: " + str(len(df))) # 64504
print("unique ID length after dropping all duplicates: " + str(len(df['Loan ID'].unique()))) # 64504

# df.to_csv("C:/Users/Runtong/OneDrive/MPP cortana competition/data_removed_duplicates.csv")

# change mapping in 'Purpose' Columns
mapping = {
        'Debt Consolidation' : 'Debt_Consolidation',
        'other': 'OTHER',
        'Home Improvements': 'Home_Improvements',
        'Other': 'OTHER',
        'Business Loan': 'Business',
        'Buy a Car': 'major_purchase',
        'Medical Bills': 'Medical_Bills',
        'Buy House': 'major_purchase',
        'Take a Trip': 'Take_a_Trip',
        'major_purchase': 'major_purchase',
        'small_business': 'Business',
        'moving': 'OTHER',
        'Educational Expenses':'OTHER',
        'wedding' :'OTHER',
        'vacation':'OTHER',
        'renewable_energy':'OTHER'    
        }
df['Purpose'] = df['Purpose'].map(mapping)
df.to_csv("C:/Users/Runtong/OneDrive/MPP cortana competition/data_removed_duplicates.csv")


