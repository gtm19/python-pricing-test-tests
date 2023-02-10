from exercises import wrangling_data
from pandas import DataFrame
import pytest

df = wrangling_data.df

class TestDataWrangling:
    def test_dw_1(self):
        assert isinstance(df, DataFrame)
        cols = df.columns
        for col in ["year", "premium", "losses", "inflation"]:
            assert col in cols
        assert sorted(df.year.to_list()) == df.year.to_list()

    def test_dw_2(self):
        actual_loss_ratio = df.get("actual_loss_ratio")
        assert actual_loss_ratio is not None
        assert actual_loss_ratio.sum() == pytest.approx(3.9414, abs=0.001)

    def test_dw_3(self):
        inflation_index = df.get("inflation_index")
        assert inflation_index is not None
        assert inflation_index.max() == pytest.approx(1.327808, abs=0.001)
        assert df.query("year == 2017").inflation_index.iloc[0] == pytest.approx(1.08243, abs=0.001)

    def test_dw_4(self):
        inflated_loss_ratio = df.get("inflated_loss_ratio")
        assert inflated_loss_ratio is not None
        assert inflated_loss_ratio.max() == pytest.approx(0.617374, abs=0.001)
        assert df.query("year == 2017").inflated_loss_ratio.iloc[0] == pytest.approx(0.462771, abs=0.001)

    def test_dw_5(self):
        assert wrangling_data.all_years_loss_ratio(df) == pytest.approx(0.441244, abs=0.001)

    def test_dw_6(self):
        assert wrangling_data.last_n_years_loss_ratio(df, 2) == pytest.approx(0.467106, abs=0.001)
        assert wrangling_data.last_n_years_loss_ratio(df, 4) == pytest.approx(0.458929, abs=0.001)
        assert wrangling_data.last_n_years_loss_ratio(df, 5) == pytest.approx(0.457773, abs=0.001)
