# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:17:31 2019

@author: ibrahim kara
"""

def normalize_column_names(x):
    '''input x is string type, return normalized name'''
    x = x.strip()
    x = x.replace(" ", "_")
    x = x.lower()
    x = x.replace("/_", "")
    return(x)

def normalize_df_columns(df):
    '''return normalized column names for the dataframe'''
    return [normalize_column_names(j) for j in df.columns]
