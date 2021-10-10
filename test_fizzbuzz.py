import fizzbuzz

import pytest

# ,2,3,4,5
@pytest.mark.parametrize(
    "num, expected",
    [
        (1, "1"),
        (2, "2"),
        (3, "fizz"),
        (4, "4"),
        (5, "buzz"),
        (6, "fizz"),
        (15, "fizzbuzz"),
    ],
)
def test_fizzbuzz(num, expected):
    assert fizzbuzz.result(num) == expected


def test_fizzbuzz_number():
    assert fizzbuzz.result(1) == "1"
    assert fizzbuzz.result(2) == "2"
    assert fizzbuzz.result(13) == "13"
    assert fizzbuzz.result(31) == "31"


def test_fizzbuzz_fizz():
    assert fizzbuzz.result(3) == "fizz"
    assert fizzbuzz.result(6) == "fizz"


def test_fizzbuzz_buzz():
    assert fizzbuzz.result(5) == "buzz"
    assert fizzbuzz.result(10) == "buzz"

def test_fizzbuzz_fizzbuzz():
    assert fizzbuzz.result(15) == "fizzbuzz"
    assert fizzbuzz.result(30) == "fizzbuzz"
