import pytest
from src.leapyears import leapyears


def test_are_leapyears_divisible_by_400():
    assert leapyears(2000) == "Are Leap years"


def test_not_leapyears_divisible_by_100_but_not_by_400():
    assert leapyears(1700) == "Not Leap years"


def test_are_leapyears_divisible_by_4_but_not_by_100():
    assert leapyears(2016) == "Are Leap years"


def test_not_leapyears_not_divisible_by_4():
    assert leapyears(2019) == "Not Leap years"
