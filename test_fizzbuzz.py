from fizzbuzz import fizzbuzz_value


def test_fizz():
    assert fizzbuzz_value(3) == "Fizz"


def test_buzz():
    assert fizzbuzz_value(5) == "Buzz"


def test_fizzbuzz():
    assert fizzbuzz_value(15) == "FizzBuzz"


def test_regular_number():
    assert fizzbuzz_value(7) == "7"