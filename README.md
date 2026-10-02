# FizzBuzz Python Project

A Python implementation of the classic **FizzBuzz programming challenge**. This project demonstrates fundamental programming concepts including loops, conditional logic, functions, the modulo operator, and automated testing with pytest.

## Features

- Processes numbers from 1 through 100
- Returns `Fizz` for numbers divisible by 3
- Returns `Buzz` for numbers divisible by 5
- Returns `FizzBuzz` for numbers divisible by both 3 and 5
- Uses reusable Python functions
- Includes automated tests with pytest
- Separates program logic from execution for easier testing and maintenance

## Technologies Used

- Python
- pytest
- Git
- GitHub
- Visual Studio Code

## Project Structure

```text
Fizzbuzz/
├── fizzbuzz.py
├── test_fizzbuzz.py
├── README.md
└── .gitignore
```

## How FizzBuzz Works

The program evaluates each number using Python's modulo operator (`%`).

If a number is divisible by both 3 and 5:

```python
number % 3 == 0 and number % 5 == 0
```

the program returns:

```text
FizzBuzz
```

If the number is divisible only by 3, it returns `Fizz`.

If the number is divisible only by 5, it returns `Buzz`.

Otherwise, the original number is returned.

## Running the Project

Clone the repository:

```bash
git clone https://github.com/tabner0320/Fizzbuzz.git
```

Navigate into the project:

```bash
cd Fizzbuzz
```

Run the program:

```bash
python fizzbuzz.py
```

## Example Output

```text
1
2
Fizz