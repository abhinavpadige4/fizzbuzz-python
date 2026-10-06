# FizzBuzz (Python)

Classic FizzBuzz implementation in Python with a small test block.

## Rules

| Condition                | Output     |
| ------------------------ | ---------- |
| Multiple of 3            | `Fizz`     |
| Multiple of 5            | `Buzz`     |
| Multiple of both (15)    | `FizzBuzz` |
| Otherwise                | the number |

## Files

- `fizzbuzz.py` — implementation + self-tests

## Usage

```bash
# Print FizzBuzz for 1..100 (default)
python fizzbuzz.py

# Print FizzBuzz for a custom range
python fizzbuzz.py 1 20
```

## API

```python
from fizzbuzz import fizzbuzz, fizzbuzz_range, run

fizzbuzz(15)        # -> "FizzBuzz"
fizzbuzz(7)         # -> "7"
fizzbuzz_range(1, 5)  # -> ["1", "2", "Fizz", "4", "Buzz"]
run(1, 100)         # prints 1..100
```

## Tests

The file includes an `assert`-based test block at the bottom that runs after
the main output. It covers:

- `3 -> "Fizz"`
- `5 -> "Buzz"`
- `15 -> "FizzBuzz"`
- `7 -> "7"`
- plus a few extra edge cases (`1`, `2`, `9`, `10`, `30`, `100`) and the
  `fizzbuzz_range` helper.

Run the file to see the assertions execute:

```bash
python fizzbuzz.py
# ...
# All FizzBuzz assertions passed.
```
