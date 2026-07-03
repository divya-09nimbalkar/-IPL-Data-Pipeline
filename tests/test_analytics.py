import pandas as pd
from src.analytics import run_analysis

def test_run_analysis():
    df = pd.DataFrame({
        "date": ["2024-04-01"],
        "team1": ["CSK"],
        "team2": ["MI"],
        "winner": ["CSK"],
        "runs_team1": [180],
        "runs_team2": [175]
    })
    results = run_analysis(df)
    assert results["matches"] == 1
    assert "CSK" in results["winners"]
