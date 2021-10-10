import fizzbuzz

import pytest

# ,2,3,4,5
@pytest.mark.parametrize(
    "num, expected", [(1, "1"), (2, "2"), (3, "fizz"), (4, "4"), (5, "buzz"), (6, "fizz"), (15, "fizzbuzz")]
)
def test_fizzbuzz(num, expected):
    assert fizzbuzz.result(num) == expected
