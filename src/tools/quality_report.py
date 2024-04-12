import pandas as pd;
import matplotlib.pyplot as plt


def categorial(df, features):
    headers = ["feature","count", "% miss.", "card.", "Mode", "Mode freq.", "Mode %", "2nd Mode", "2nd Mode freq.", "2nd Mode %"]
    report = []
    for feature in features:
        report.append([
            feature,
            df[feature].size,
            df[feature].isnull().sum() / df[feature].size,
            df[feature].nunique(),
            df[feature].mode().values[0],
            df[feature].value_counts().max(),
            (df[feature].value_counts().max() / df[feature].size) * 100,
            df[feature].value_counts().index[1],
            df[feature].value_counts().iloc[1],
            (df[feature].value_counts().iloc[1] / df[feature].size) * 100,
        ])
    return pd.DataFrame(report, columns=headers)


def continues(df, features):
    headers = ["feature","count", "% miss.", "card.", "min", "1st Qrt.", "mean", "median", "3rd Qrt.", "max", "std dev."] 
    report = []
    for feature in features:
        report.append([
            feature,
            df[feature].size,
            (df[feature].isnull().sum() / df[feature].size) * 100,
            df[feature].nunique(),
            df[feature].min(),
            df[feature].quantile(0.25),
            df[feature].mean(),
            df[feature].median(),
            df[feature].quantile(0.75),
            df[feature].max(),
            df[feature].std(),
        ])
    return pd.DataFrame(report, columns=headers)

def graphs(plot_func, features, cols=4, height=6):
    rows = ceildiv(len(features), cols)
    _, axes = plt.subplots(nrows=rows,ncols=cols, figsize=(20, height*rows))
    plt.subplots_adjust(hspace=0.5)
    for i, feature in enumerate(features):
        loc = axes[i // cols, i % cols] if rows > 1 and cols > 1 else axes[i % cols]
        plot_func(feature, loc)
    return plt 
        

def ceildiv(a, b):
    return -(a // -b)