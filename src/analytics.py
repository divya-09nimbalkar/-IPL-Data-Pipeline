import pandas as pd

def run_analysis(df: pd.DataFrame) -> dict:
    """Return basic stats."""
    return {
        "matches": len(df),
        "teams": sorted(set(df["team1"]).union(df["team2"])),
        "most_runs_team1": df["runs_team1"].max(),
        "most_runs_team2": df["runs_team2"].max(),
        "winners": df["winner"].value_counts().to_dict()
    }
