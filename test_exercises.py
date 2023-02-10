import pytest
import builtins
import os

import logging

from exercises import exercises

LOGGER = logging.getLogger(__name__)

# Utilities
def get_type(type_name):
        return getattr(builtins, type_name, None)

# tests
class TestExercises:
    def test_ex_1(self):
        assert exercises.exposure == 150

    def test_ex_2(self, capsys):
        with pytest.raises(Exception):
            exercises.validate_exposure(-10)

        capsys.readouterr()

        exercises.validate_exposure(5)
        out, err = capsys.readouterr()
        print(out)
        assert 'small' in out.lower()

        capsys.readouterr()

        exercises.validate_exposure(105)
        out, err = capsys.readouterr()
        print(out)
        assert 'large' in out.lower()

    def test_ex_3(self):
        policy_info = exercises.policy_info
        assert type(policy_info) is dict
        assert policy_info.get("policy_ref").upper() == "ABC1"
        assert policy_info.get("business_class").lower() == "property"
        assert policy_info.get("year") == 2022

        assert exercises.policy_year == policy_info.get("year")

    def test_ex_4(self):
        assert exercises.vehicles == [
            "car",
            "plane",
            "boat",
            "train"
        ]

    def test_ex_4(self):
        user_type = exercises.a_variable_type

        if type(user_type) is not type:
            user_type = get_type(str(user_type))

        assert user_type is type(60.8)

    def test_ex_5(self):
        premium_rater = exercises.premium_rater

        # test for errors
        for (exp, rate) in [
            ("a", 1),
            (10, "a"),
            ("g", "a"),
            (10, -30),
            (-20, 10),
            (-100, -1000)
        ]:
            with pytest.raises(ValueError):
                premium_rater(exp, rate)

        # test for rate uplift
        assert premium_rater(15e6, 0.5) == pytest.approx(8_250_000, abs=1e-5)
        # test for smaller exposures
        assert premium_rater(1000, 0.1) == pytest.approx(100, abs=1e-5)

    # Bonus question checking
    if os.path.exists("tests") and len(os.listdir("tests")) > 0:
        LOGGER.info("Unit tests exist in tests/. Check them out!")
    else:
        LOGGER.warn("No unit tests have been created for bonus question")
