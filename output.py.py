def save_data(df, path):
    df.to_csv(path, index=False)