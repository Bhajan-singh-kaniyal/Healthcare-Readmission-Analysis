import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    # Drop duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.fillna(method='ffill')

    # Convert target column
    df['readmitted'] = df['readmitted'].apply(
        lambda x: 1 if x == '<30' else 0
    )

    return df

def save_data(df, path):
    df.to_csv(path, index=False)
