import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean IPL match data:
    - Drop rows with missing values
    - Convert date column to datetime
    """
    df = df.dropna()
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])
    return df
