# -*- coding: utf-8 -*-
"""
Created on Sun Apr 09 11:15:39 2017

@author: Runtong
"""

def test_data_processing(df):
    import pandas as pd
    from datetime import date
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
    df.drop(axis=1, labels=drop_list, inplace=True)
    df.drop_duplicates(inplace=True)
    df.reset_index(drop=True, inplace=True)
    
    cateogrical_val_list = [
            'City',
            'StateProvinceName',
            'CountryRegionName',
            'Education',
            'Occupation',
            'Gender',
            'MaritalStatus',
            'HomeOwnerFlag',
            ]
    for items in cateogrical_val_list:
        df[items] = df[items].astype('category')
    
    import math
    df.BirthDate = pd.to_datetime(df.BirthDate)
    df['age'] = (date(2017,3,6)-df.BirthDate.dt.date).apply(lambda x: math.floor(x.days/365))
    
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
            ]
    for items in cateogrical_val_list:
        df[items] = df[items].astype('category')
    
    #Drop BirthDate and non-influential parameters
    df.drop(axis=1, labels=['CustomerID','BirthDate', 'City','StateProvinceName','CountryRegionName',], inplace=True)
    return df