import numpy as np
from tools import stream as str

class Stream:
    def __init__(self, series):
        self.series = series

    def reduce(self, func, initial):
        result = initial
        for item in self.series:
            result = func(result, item)
        return result

    def sum(self, func):
        result = 0
        for item in self.series:
            result = result + func(item)
        return result
    
    @staticmethod
    def of(series): 
        return Stream(series)
    
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
    return Stream.of(features).reduce(lambda data, feature: _scale(data, feature), df)
