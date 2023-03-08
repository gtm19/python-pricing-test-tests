import pytest

def pytest_emoji_passed(config):
    return "✅", "PASSED ✅ "

def pytest_emoji_failed(config):
    return "🚨", "FAILED 🚨 "

def check_year_value(df, year:int, col:str, expected, tolerance=0.001):
    actual = df.query(f"year == {year}")[col].iloc[0]
    return actual == pytest.approx(expected, abs=tolerance)
