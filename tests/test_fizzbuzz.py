import pytest
from src.fizzbuzz import fizzbuzz


def test_fizzbuzz_multiple_of_3():
    assert fizzbuzz(3) == "fizz"


def test_fizzbuzz_multiple_of_5():
    assert fizzbuzz(5) == "buzz"


def test_fizzbuzz_multiple_of_3_and_5():
    assert fizzbuzz(15) == "fizzbuzz"
