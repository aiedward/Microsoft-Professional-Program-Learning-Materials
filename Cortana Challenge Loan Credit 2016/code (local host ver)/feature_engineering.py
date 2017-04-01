# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 16:41:21 2017

@author: Runtong
"""
import pandas as pd
df = pd.read_csv("C:/Users/Runtong/OneDrive/MPP cortana competition/data_removed_duplicates_Updated.csv",header=0)

#---------------------#
# scattered matrix check data distribution and relationship
def scatter_matrix_PLOT(df):
    import matplotlib.pyplot as plt
    from pandas.tools.plotting import scatter_matrix
    fig = plt.figure(figsize=(20, 20))
    fig.clf()
    ax = fig.gca()
    scatter_matrix(df, alpha=0.3, 
                   diagonal='kde', ax = ax)
    return 'Done'

# scatter_matrix_PLOT(df)


# hist plot to check the distribution of data
def hist_PLOT(series):
    series.plot.hist(bins = 20, alpha = 0.7)
    return "Done"




# Conditional Histograms: check the relationship between label and one single factor
def cond_hist_PLOT(series):
    import matplotlib.pyplot as plt
    df_plot = pd.concat([df[series], df['Loan Status']], axis=1)
    list = df_plot[df_plot.columns[0]].unique()
    # Plot
    fig, ax = plt.subplots(nrows=len(list), figsize=(len(list), 2.5*len(list)))
    num = 0
    for item in list:     
        data = df_plot[df_plot[df_plot.columns[0]]==item]["Loan Status"]
        ax[num].hist(data, bins = 2, alpha = 0.5)
        ax[num].set_title('Loan Status conditioned by ' + str(item)  + '\n')
        num = num + 1
    plt.tight_layout()
    plt.show()
    return "Done"

cond_hist_PLOT('Months since last delinquent')
# Scatter plot to show outlier and relationship with label
def scatter_PLOT(series):
    import matplotlib.pyplot as plt
    plt.scatter(df[series], df['Loan Status'],alpha=0.5)
    plt.title(series + ' w.r.t Loan Status')
    plt.xlim(-1,2)
    plt.xlabel(series)
    plt.ylabel('Loan Status')
    plt.show()
    return "Done"

numerical_var = ['Annual Income']
for items in numerical_var:
    scatter_PLOT(items)
#---------------------#
# Part II: Feature Engineering

# make categorical:
    # Label: Loan Status (30% CHARGED_OFF, 70% FULLY_PAID)
    # Wrongly categorize CHARGED_OFF to FULLY_PAID is more severe than the reverse.
    # Therefore, Flase Negative/Type II more severe than Flase Positive/Type I
    
    # RECALL very important, more important than precision
df['Loan Status'] = df['Loan Status'].map({'Charged Off':1, 'Fully Paid':0})

    # Current Loan Amount is roughly normal, need simple normalization
from sklearn import preprocessing
df['Current Loan Amount'] = preprocessing.StandardScaler().fit_transform(df['Current Loan Amount'])

    # Term: make categorical
df['Term'] = df['Term'].astype("category").cat.codes
  
    # Credit Score: highly skewed towards right
import numpy as np
ln = pd.DataFrame(np.log(df['Credit Score'].as_matrix()))
df['Credit Score'] = pd.DataFrame(preprocessing.MaxAbsScaler().fit_transform(ln))

    # Years in current job, merge to 3 categories, with each one approximately 20000 instances
#mapping_years = {
#        '10+ years': '10+ years',
#        '2 years': '3- years',
#        '3 years': '3- years',
#        '< 1 year': '3- years',
#        '5 years': '3+ years',
#        '1 year': '3- years',
#        '4 years': '3+ years',
#        '6 years': '3+ years',
#        '7 years' : '3+ years',
#        '8 years': '3+ years',
#        '9 years': '3+ years'
#        }
#df['Years in current job'] = df['Years in current job'].map(mapping_years)

    # Annual Income: there are only 200+ samples above 3*10^6, so trim them
df['Annual Income'] = df['Annual Income'].clip(upper=250000)
# normalize the income
df['Annual Income'] = preprocessing.StandardScaler().fit_transform(df['Annual Income'])

    # Monthly Debt: trim above 4000
df['Monthly Debt'] = df['Monthly Debt'].clip(upper=4000)
df['Monthly Debt'] = preprocessing.StandardScaler().fit_transform(df['Monthly Debt'])

    # Years of Credit History: trim above 40
df['Years of Credit History'] = df['Years of Credit History'].clip(upper=40)
df['Years of Credit History'] = preprocessing.StandardScaler().fit_transform(df['Years of Credit History'])  
    
    
    # Months since last delinquent: trim above 80
# df['Months since last delinquent'] = df['Months since last delinquent'].clip(upper=80)
# many missing values, map them to -1
# df['Months since last delinquent'] = df['Months since last delinquent'].fillna(value=-1)
# df['Months since last delinquent'] = preprocessing.StandardScaler().fit_transform(df['Months since last delinquent'])  

# check if distribution is uniform
# df['check'] = df['Months since last delinquent'].apply(lambda x: -1 if x <=60 else 0)         
# cond_hist_PLOT('check')       
# Conclusion: mostly same, can be deleted

    # Number of Open Accounts: trim above 25
df['Number of Open Accounts'] = df['Number of Open Accounts'].clip(upper=25)
df['Number of Open Accounts'] = preprocessing.StandardScaler().fit_transform(df['Number of Open Accounts']) 

    # Number of Credit Problems: make categorical
df['Number of Credit Problems'] = df['Number of Credit Problems'].apply(lambda x: x if x==0  else 1)  

    # Current Credit Balance: trim at 80000
df['Current Credit Balance'] = df['Current Credit Balance'].clip(upper=80000)
df['Current Credit Balance'] = preprocessing.StandardScaler().fit_transform(df['Current Credit Balance']) 

    # Maximum Open Credit: 
df['Maximum Open Credit'] = df['Maximum Open Credit'].clip(upper=100000)       
df['Maximum Open Credit'] = preprocessing.StandardScaler().fit_transform(df['Maximum Open Credit']) 

    # Bankruptcies and Tax Liens
df['Bankruptcies'] = df['Bankruptcies'].apply(lambda x: x if x==0  else 1)  
df['Tax Liens'] = df['Tax Liens'].apply(lambda x: x if x==0  else 1) 

# hist_PLOT(df['Maximum Open Credit'])

categorical_var = ['Years in current job','Home Ownership', 'Purpose']
for items in categorical_var:
    cond_hist_PLOT(items)
    
numerical_var = ['Annual Income','Monthly Debt']
for items in numerical_var:
    scatter_PLOT(items)








