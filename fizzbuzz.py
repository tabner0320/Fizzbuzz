def fizzbuzz_value(number):
    """Return the FizzBuzz value for a given number."""
    
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)


def run_fizzbuzz(start=1, end=100):
    """Run FizzBuzz for a range of numbers."""
    
    for number in range(start, end + 1):
        print(fizzbuzz_value(number))


if __name__ == "__main__":
    run_fizzbuzz()