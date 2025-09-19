"""
screentime.py
-------------
Handles loading and analyzing screen time data for Focus Zone AI.

This file provides functions to:
- Load screentime data from a CSV file (default: `screentime.csv`)
- Calculate the average daily usage in hours

Functions:
- load_screentime(file_path: str = "screentime.csv") -> pd.DataFrame | None
    Loads screentime data from a CSV file. Returns a pandas DataFrame or None if failed.

- calculate_average_hours(df: pd.DataFrame) -> float
    Calculates the average screen time in hours from a DataFrame with a "minutes" column.
    Returns 0 if the DataFrame is empty or None.
"""

import pandas as pd

SCREENTIME_FILE = "screentime.csv"

def load_screentime(file_path="screentime.csv"):
    """Load screentime data from CSV. Returns a DataFrame or None on error."""
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print("Error reading CSV:", e)
        return None

def calculate_average_hours(df):
    """Calculate average screen time in hours from DataFrame. Returns 0 if invalid."""
    if df is None or df.empty:
        return 0
    return df["minutes"].mean() / 60

def save_screentime(df: pd.DataFrame):
    """Save DataFrame to CSV, overwriting existing screentime data."""
    df.to_csv(SCREENTIME_FILE, index=False)

def daily_average(df: pd.DataFrame):
    """Return average screen time per day in hours."""
    if df is None or df.empty:
        return {}
    return (df.groupby("date")["minutes"].sum() / 60).to_dict()

