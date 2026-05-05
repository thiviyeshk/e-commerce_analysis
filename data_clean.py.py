import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)

    # Handle missing values
    df['Age'].fillna(df['Age'].mean(), inplace=True)
    df = df.dropna()

    # Remove duplicates
    df = df.drop_duplicates()

    # Clean column names
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(" ", "_")

    # Convert data types
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    df['purchase_amount'] = pd.to_numeric(df['purchase_amount'])

    return df