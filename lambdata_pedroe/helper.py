import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

df = pd.DataFrame([1,2,3])

def null_check(dataframe):
    series = dataframe.isnull().any()
    null_columns = pd.Dataframe(series, columns=['Nulls'])
    null = False
    for i in range(len(null_columns)):
        if null_columns['Nulls'].iloc[i] == True:
            print('Column', '"', null_columns.index[i], '"', 'contains null values')
            null = True
    if null == False:
        print('Nno null values')

def train_test_val_split(dataframe):
    train, test = train_test_split(dataframe, train_size=0.8)
    train, val = train_test_split(train, train_size=0.4)
    return train, val, test