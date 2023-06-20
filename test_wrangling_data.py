from exercises import wrangling_data
from .conftest import check_year_value
from pandas import DataFrame
import pytest

df = wrangling_data.df


# TESTS
class TestDataWrangling01:
    def test_df_is_df(self):
        assert isinstance(df, DataFrame)

    def test_df_has_right_columns(self):
        expected_cols = set(["year", "premium", "losses", "inflation"])
        observed_cols = set(df.columns)
        assert expected_cols.issubset(observed_cols)

    def test_df_is_sorted(self):
        assert sorted(df.year.to_list()) == df.year.to_list()


class TestDataWrangling02:
    def test_columns_present(self):
        assert "actual_loss_ratio" in df.columns

    @pytest.mark.parametrize(
        "year,expected",
        zip(
            range(2014, 2023),
            [
                0.400,
                0.412,
                0.416,
                0.428,
                0.452,
                0.456,
                0.444,
                0.469,
                0.465,
            ],
        ),
    )
    def test_actual_loss_ratio(self, year, expected):
        check_year_value(df, year, "actual_loss_ratio", expected)


class TestDataWrangling03:
    def test_columns_present(self):
        assert "inflation_index" in df.columns

    @pytest.mark.parametrize(
        "year,expected",
        zip(
            range(2014, 2023),
            [
                1.328,
                1.302,
                1.276,
                1.251,
                1.227,
                1.203,
                1.168,
                1.134,
                1.090,
            ],
        ),
    )
    def test_inflation_index(self, year, expected):
        check_year_value(df, year, "inflation_index", expected)


class TestDataWrangling04:
    def test_columns_present(self):
        assert "inflated_loss_ratio" in df.columns

    @pytest.mark.parametrize(
        "year,expected",
        zip(
            range(2014, 2023),
            [
                0.531,
                0.536,
                0.530,
                0.535,
                0.555,
                0.549,
                0.518,
                0.532,
                0.507,
            ],
        ),
    )
    def test_inflated_loss_ratio(self, year, expected):
        check_year_value(df, year, "inflated_loss_ratio", expected)


class TestDataWrangling05:
    def all_years_lr_correct(self):
        assert wrangling_data.all_year_loss_ratio(df) == pytest.approx(0.441, abs=0.001)


class TestDataWrangling06:
    @pytest.mark.parametrize(
        "n,expected",
        zip(
            range(9, 0, -1),
            [0.441, 0.445, 0.449, 0.453, 0.458, 0.459, 0.460, 0.467, 0.465],
        ),
    )
    def last_n_years_lr_correct(self, n, expected):
        assert wrangling_data.last_n_year_loss_ratio(df, n) == pytest.approx(
            expected, abs=0.001
        )
