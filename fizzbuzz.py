"""FizzBuzz implementation in Python.

Rules:
    - Multiples of 3  -> "Fizz"
    - Multiples of 5  -> "Buzz"
    - Multiples of 15 -> "FizzBuzz"
    - Otherwise       -> the number itself (as a string)

Usage:
    python fizzbuzz.py            # prints 1..100
    python fizzbuzz.py 1 20       # prints 1..20
"""

from __future__ import annotations

from typing import List


def fizzbuzz(n: int) -> str:
    """Return the FizzBuzz string for a single integer ``n``.

    Args:
        n: The integer to evaluate.

    Returns:
        "FizzBuzz" if n is divisible by both 3 and 5,
        "Fizz" if divisible by 3 only,
        "Buzz" if divisible by 5 only,
        otherwise the string representation of ``n``.
    """
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def fizzbuzz_range(start: int, end: int) -> List[str]:
    """Return a list of FizzBuzz strings for the inclusive range [start, end]."""
    return [fizzbuzz(i) for i in range(start, end + 1)]


def run(start: int = 1, end: int = 100) -> None:
    """Print the FizzBuzz sequence for the inclusive range [start, end]."""
    for value in fizzbuzz_range(start, end):
        print(value)


if __name__ == "__main__":
    # Default behaviour: print FizzBuzz for 1..100
    run(1, 100)

    # ------------------------------------------------------------------
    # Self-tests: verify the core logic for representative cases.
    # These run after the main output so they don't pollute the sequence.
    # ------------------------------------------------------------------
    assert fizzbuzz(1) == "1", "1 should map to '1'"
    assert fizzbuzz(2) == "2", "2 should map to '2'"
    assert fizzbuzz(3) == "Fizz", "3 should map to 'Fizz'"
    assert fizzbuzz(5) == "Buzz", "5 should map to 'Buzz'"
    assert fizzbuzz(7) == "7", "7 should map to '7'"
    assert fizzbuzz(9) == "Fizz", "9 should map to 'Fizz'"
    assert fizzbuzz(10) == "Buzz", "10 should map to 'Buzz'"
    assert fizzbuzz(15) == "FizzBuzz", "15 should map to 'FizzBuzz'"
    assert fizzbuzz(30) == "FizzBuzz", "30 should map to 'FizzBuzz'"
    assert fizzbuzz(100) == "Buzz", "100 should map to 'Buzz'"

    # Range helper sanity check
    assert fizzbuzz_range(1, 5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert fizzbuzz_range(13, 17) == ["13", "Fizz", "Buzz", "FizzBuzz", "17"]

    print("\nAll FizzBuzz assertions passed.")
