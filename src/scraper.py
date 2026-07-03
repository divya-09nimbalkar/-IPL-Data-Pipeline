import pandas as pd
from pathlib import Path

def fetch_mock_matches() -> pd.DataFrame:
    data_path = Path(__file__).resolve().parent.parent / "data" / "raw" / "ipl_matches.csv"
    return pd.read_csv(data_path)
