import pandas as pd
from src.processor import clean_data

def test_clean_data():
    df = pd.DataFrame({"date": ["2024-04-01", None], "team1": ["CSK", None]})
    cleaned = clean_data(df)
    assert cleaned.isnull().sum().sum() == 0
    