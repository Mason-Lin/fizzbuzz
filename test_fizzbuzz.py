import fizzbuzz


def test_fizzbuzz():
    assert fizzbuzz.result(1) == "1"
    assert fizzbuzz.result(2) == "2"
    assert fizzbuzz.result(3) == "fizz"
    assert fizzbuzz.result(4) == "4"
    assert fizzbuzz.result(5) == "buzz"
