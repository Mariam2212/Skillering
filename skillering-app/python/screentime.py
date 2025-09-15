import pandas as pd

def load_screentime(file_path="screentime.csv"):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print("Error reading CSV:", e)
        return None

def calculate_average_hours(df):
    if df is None or df.empty:
        return 0
    return df["minutes"].mean() / 60
