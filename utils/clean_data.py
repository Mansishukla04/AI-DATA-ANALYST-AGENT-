import pandas as pd

def clean_dataset(df):
    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing values
    df = df.fillna("Unknown")

    return df