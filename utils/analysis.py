import pandas as pd

def get_dataset_summary(df):

    summary = {
        "Total Rows": df.shape[0],
        "Total Columns": df.shape[1],
        "Missing Values": df.isnull().sum().sum(),
        "Duplicate Rows": df.duplicated().sum()
    }

    return summary