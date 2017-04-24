# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 16:53:21 2017

@author: Runtong
"""

import pandas as pd
from datetime import date
data_path = "C:/Users/Runtong/OneDrive/MPP capstone project 2017/AWCustomers/AWJoined.csv"
df = pd.read_csv(data_path)

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
        'BikeBuyer'
        ]
for items in cateogrical_val_list:
    df[items] = df[items].astype('category')

# BirthDate:
# Transform to the measurement of Age, while keep Year/Month/Day variables separate
import math
df.BirthDate = pd.to_datetime(df.BirthDate)
df['age'] = (date(2017,3,6)-df.BirthDate.dt.date).apply(lambda x: math.floor(x.days/365))
df['year'] = df.BirthDate.apply(lambda x: x.year)
df['month'] = df.BirthDate.apply(lambda x: x.month)
df['day'] = df.BirthDate.apply(lambda x: x.day)

# peek into datatypes and basic stats
print df.dtypes
print df.describe()

# Scatter Plot: AvgMonthSpend vs. Age, legend: Male & Female
def plot_scatter():
    # create a sample of size 200
    df_sample = df.sample(n=400)
    import matplotlib.pyplot as plt
    colors = ['b', 'c', 'y', 'm', 'r']
    plt.scatter(df_sample[df_sample.Gender=='M'].age,df_sample[df_sample.Gender=='M'].AvgMonthSpend, marker='o', color=colors[1])
    plt.scatter(df_sample[df_sample.Gender=='F'].age,df_sample[df_sample.Gender=='F'].AvgMonthSpend, marker='x', color=colors[4])
    plt.legend(("Male","Female"),scatterpoints=1,
           loc='lower left',
           ncol=3,
           fontsize=8)
    plt.xlabel("Age")
    plt.ylabel("AvgMonthSpend")
    plt.title("AvgMonthSpend vs. Age")
    plt.show()

#plot_scatter()

# Histogram on different categorical values
def hist_AvgMonthSpend_plot(items):
    df_sample = df.sample(n=400)
    import matplotlib.pyplot as plt
    category=df_sample[items].unique()
    for entry in category:
        plt.hist(df_sample[df_sample[items]==entry].AvgMonthSpend, bins=10, alpha=0.3)
    plt.title("AvgMonthSpend vs. %s"%items)
    plt.xlabel("AvgMonthSpend")
    plt.ylabel("count")
    plt.legend(category, fontsize=8)
    plt.xlim([df_sample['AvgMonthSpend'].min(), df_sample['AvgMonthSpend'].max()])
    plt.show()

hist_plot_list = ['CountryRegionName','Education','Occupation','Gender','MaritalStatus',
                  'NumberChildrenAtHome','TotalChildren', 'NumberCarsOwned']
for name in hist_plot_list:
    hist_AvgMonthSpend_plot(name)



# A series of histogram for different legend vs. BikeBuyer
def hist_BikeBuyer_plot(items):
    df_sample = df.sample(n=400)
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
    columns = df_sample[items].unique()
    f, axarr = plt.subplots(1, len(columns))
    for num in range(0,len(columns)):
        axarr[num].hist(df_sample[df_sample[items]==columns[num]].BikeBuyer, bins=2, alpha=0.3)
        if num != 0:
            plt.setp(axarr[num].get_yticklabels(), visible=False)
#            plt.setp(axarr[num].get_xticklabels(), visible=False)
        axarr[num].xaxis.set_major_locator(ticker.MultipleLocator(1.0))
        axarr[num].yaxis.set_label_position("left")
        axarr[num].set_ylabel(columns[num])
    f.subplots_adjust(hspace=0.5)
    f.suptitle(items, fontsize=12)
    plt.tight_layout()
    plt.show()

hist_plot_list = ['CountryRegionName','Education','Occupation','Gender','MaritalStatus',
                  'NumberChildrenAtHome','TotalChildren', 'NumberCarsOwned']
for name in hist_plot_list:
    hist_BikeBuyer_plot(name)


# Apparent Correlations with AvgMonthlySpend
df[df.MaritalStatus=='M'].AvgMonthSpend.median() > df[df.MaritalStatus=='S'].AvgMonthSpend.median()
df[df.NumberCarsOwned==0].AvgMonthSpend.median() > df[df.NumberCarsOwned!=0].AvgMonthSpend.median()
df[df.Gender=='M'].AvgMonthSpend.median() > df[df.Gender=='F'].AvgMonthSpend.median()
df[df.NumberChildrenAtHome==0].AvgMonthSpend.median() < df[df.NumberChildrenAtHome!=0].AvgMonthSpend.median()

# Correlations with BikeBuyer
df[df.BikeBuyer!=0].YearlyIncome.median() > df[df.BikeBuyer==0].YearlyIncome.median()
df[df.BikeBuyer!=0].NumberCarsOwned.median() < df[df.BikeBuyer==0].NumberCarsOwned.median()
for job in df.Occupation.unique():
    print job
    print ((df.Occupation==job) & (df.BikeBuyer==1)).sum() 

((df.Gender=='M') & (df.BikeBuyer==1)).sum() > ((df.Gender=='F') & (df.BikeBuyer==1)).sum()
((df.MaritalStatus=='S') & (df.BikeBuyer==1)).sum() > ((df.MaritalStatus=='M') & (df.BikeBuyer==1)).sum()

df.to_csv("C:/Users/Runtong/OneDrive/MPP capstone project 2017/AWCustomers/AWJoined_after_wrangling.csv")