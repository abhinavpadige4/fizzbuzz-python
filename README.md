# FizzBuzz in Python

A clean Python implementation of the classic FizzBuzz interview problem.

## Rules

- Multiples of **3** → `Fizz`
- Multiples of **5** → `Buzz`
- Multiples of **both 3 and 5** → `FizzBuzz`
- Otherwise → the number itself

## Files

- `fizzbuzz.py` — Implementation with `fizzbuzz(n)` function, a `run_fizzbuzz(start, end)` runner, and a `run_tests()` suite of `assert` statements covering all four cases.

## Usage

Run the script directly to execute the test suite and then print FizzBuzz for 1–100:

```bash
python fizzbuzz.py
```

Or import the function:

```python
from fizzbuzz import fizzbuzz

print(fizzbuzz(3))   # Fizz
print(fizzbuzz(5))   # Buzz
print(fizzbuzz(15))  # FizzBuzz
print(fizzbuzz(7))   # 7
```

## Tests

The `run_tests()` function asserts the expected output for a wide range of inputs:

- Multiples of 3 only (3, 6, 9, 12, 18)
- Multiples of 5 only (5, 10, 20, 25)
- Multiples of both (15, 30, 45, 60, 75, 90)
- Plain numbers (1, 2, 4, 7, 8, 11, 13, 97, 100)

Run the tests in isolation:

```bash
python -c "from fizzbuzz import run_tests; run_tests()"
```

## Complexity

- **Time:** O(1) per call (constant-time modulo checks)
- **Space:** O(1)
