from src.scraper import fetch_mock_matches

def test_fetch_mock_matches():
    df = fetch_mock_matches()
    assert not df.empty
    assert "winner" in df.columns
