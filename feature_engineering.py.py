def add_time_features(df):
    df['month'] = df['transaction_date'].dt.month
    df['year'] = df['transaction_date'].dt.year
    
    return df