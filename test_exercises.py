import pytest
import builtins
import os
import random

from exercises import exercises

# Utilities
def get_type(type_name):
        return getattr(builtins, type_name, None)

class TestEx01:
    def test_exposure(self):
        assert exercises.exposure == 150

class TestEx02:
    def test_validate_exposure_error(self):
        with pytest.raises(Exception):
            exercises.validate_exposure(-10)

    @pytest.mark.parametrize(
        "value,text",
        [
            (5, "small"),
            (105, "large"),
        ]
    )
    def test_validate_exposure_small(self, capsys, value, text):
        capsys.readouterr()

        exercises.validate_exposure(value)
        out, err = capsys.readouterr()
        print(out)
        assert text in out.lower()

    def test_validate_exposure_large(self, capsys):
        capsys.readouterr()

        exercises.validate_exposure(105)
        out, err = capsys.readouterr()
        print(out)
        assert 'large' in out.lower()

class TestEx03:
    def test_policy_info_dict(self):
        assert type(exercises.policy_info) is dict

    def test_policy_info_content(self):
        assert exercises.policy_info.get("policy_ref").upper() == "ABC1"
        assert exercises.policy_info.get("business_class").lower() == "property"
        assert isinstance(exercises.policy_info.get("year"), (int, float))
        assert exercises.policy_info.get("year") == 2022

    def test_policy_year_assignment(self):
        assert exercises.policy_year == exercises.policy_info.get("year")

class TestEx04:
    def test_vehicles(self):
        assert exercises.vehicles == [
            "car",
            "plane",
            "boat",
            "train"
        ]

class TestEx05:
    def test_type(self):
        user_type = exercises.a_variable_type

        if type(user_type) is not type:
            user_type = get_type(str(user_type))

        assert user_type is type(60.8)

class TestEx06:
    @pytest.mark.parametrize(
        "exp,rate",
        [
            ("a", 1),
            (10, "a"),
            ("g", "a"),
            (10, -30),
            (-20, 10),
            (-100, -1000)
        ]
    )
    def test_premium_rater_errors(self, exp, rate):
        with pytest.raises(ValueError):
            exercises.premium_rater(exp, rate)

    @pytest.mark.parametrize(
        "exp,rate,expected_uplift",
        [
            (1.5e7, 0.5, 0.1),
            (2e6, 0.5, 0.1),
            (5e5, 0.2, 0),
            (1e3, 0.1, 0),
        ]
    )
    def test_premium_rater_calcs(self, exp, rate, expected_uplift):
        calced_uplift = (exercises.premium_rater(exp, rate) / (exp * rate)) - 1
        assert round(calced_uplift, 2) == pytest.approx(expected_uplift, abs=1e-2)

class TestEx07:
    def test_counter(self):
        counter = exercises.Counter()
        n = random.choice(range(50)) + 1
        [ counter.count_up() for _ in range(n) ]
        assert counter.count == n

class TextBonus:
    def test_unit_test_folder_exists(self):
        assert os.path.exists("tests")

    def test_unit_test_folder_not_empty(self):
        assert len(os.listdir("tests")) > 0
