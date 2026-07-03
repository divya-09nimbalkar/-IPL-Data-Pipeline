from src.utils import log_message
from src.scraper import fetch_mock_matches
from src.processor import clean_data
from src.analytics import run_analysis
from src.visualization import plot_runs, plot_winners

def main():
    log_message("Starting IPL Data Pipeline...")

    # Step 1: Fetch (mock for now)
    df = fetch_mock_matches()

    # Step 2: Clean
    df = clean_data(df)

    # Step 3: Analyze
    results = run_analysis(df)
    log_message(f"Analysis Results: {results}")

    # Step 4: Visualize
    plot_runs(df)
    plot_winners(df)

    log_message("Pipeline finished successfully.")

if __name__ == "__main__":
    main()
