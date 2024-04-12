import numpy as np
import pandas as pd
import math
from tools import stream as str

def _scale(df, feature):
    # dataframe[feature].mean()
    mean = df[feature].sum() / df[feature].size
    
    # variance = dataframe[feature].var(ddof=1)
    variance = str.of(df[feature]).sum(lambda row: pow(row - mean, 2)) / (df[feature].size - 1)

    # standard_deviation = dataframe[feature].std(ddof=1)
    standard_deviation = np.sqrt(variance / df[feature].size)

    df[feature] = df[feature].apply(lambda row: (row - mean) / standard_deviation)
    return df

def scale(df, features): 
    return str.of(features).reduce(lambda data, feature: _scale(data, feature), df)
    
def encode(df, features):
    return pd.get_dummies(df, columns=features)

def boxplot_vals(df, feature): 
    Q1 = df[feature].quantile(0.25)
    mean = df[feature].mean()
    Q3 = df[feature].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return lower_bound, Q1, mean, Q3, upper_bound

def value_freq_perc(df, feature, value):
    total_count = len(df[feature])
    value_count = len(df[df[feature] == value])
    percentage = (value_count / total_count) * 100
    return percentage

def P(occurances, total):
    return occurances / total

