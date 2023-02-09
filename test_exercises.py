import pytest
# dev mode:
# from exercises import solutions as exercises

# prod:
from exercises import exercises

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
