"""
FizzBuzz - Classic Interview Problem

Rules:
    - For multiples of 3, print 'Fizz'
    - For multiples of 5, print 'Buzz'
    - For multiples of both 3 and 5, print 'FizzBuzz'
    - Otherwise, print the number itself
"""


def fizzbuzz(n):
    """
    Return the FizzBuzz result for a given integer n.

    Args:
        n (int): The number to evaluate.

    Returns:
        str or int: 'FizzBuzz' if divisible by both 3 and 5,
                    'Fizz' if divisible by 3,
                    'Buzz' if divisible by 5,
                    otherwise the number n itself.
    """
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n


def run_fizzbuzz(start=1, end=100):
    """
    Run the FizzBuzz logic for a range of numbers and print results.

    Args:
        start (int): Starting number (inclusive). Default is 1.
        end (int): Ending number (inclusive). Default is 100.
    """
    for i in range(start, end + 1):
        print(fizzbuzz(i))


def run_tests():
    """
    Run a series of assert statements to verify the FizzBuzz logic
    against known cases.
    """
    # Multiples of 3 only
    assert fizzbuzz(3) == "Fizz", f"Expected 'Fizz' for 3, got {fizzbuzz(3)}"
    assert fizzbuzz(6) == "Fizz", f"Expected 'Fizz' for 6, got {fizzbuzz(6)}"
    assert fizzbuzz(9) == "Fizz", f"Expected 'Fizz' for 9, got {fizzbuzz(9)}"
    assert fizzbuzz(12) == "Fizz", f"Expected 'Fizz' for 12, got {fizzbuzz(12)}"
    assert fizzbuzz(18) == "Fizz", f"Expected 'Fizz' for 18, got {fizzbuzz(18)}"

    # Multiples of 5 only
    assert fizzbuzz(5) == "Buzz", f"Expected 'Buzz' for 5, got {fizzbuzz(5)}"
    assert fizzbuzz(10) == "Buzz", f"Expected 'Buzz' for 10, got {fizzbuzz(10)}"
    assert fizzbuzz(20) == "Buzz", f"Expected 'Buzz' for 20, got {fizzbuzz(20)}"
    assert fizzbuzz(25) == "Buzz", f"Expected 'Buzz' for 25, got {fizzbuzz(25)}"

    # Multiples of both 3 and 5
    assert fizzbuzz(15) == "FizzBuzz", f"Expected 'FizzBuzz' for 15, got {fizzbuzz(15)}"
    assert fizzbuzz(30) == "FizzBuzz", f"Expected 'FizzBuzz' for 30, got {fizzbuzz(30)}"
    assert fizzbuzz(45) == "FizzBuzz", f"Expected 'FizzBuzz' for 45, got {fizzbuzz(45)}"
    assert fizzbuzz(60) == "FizzBuzz", f"Expected 'FizzBuzz' for 60, got {fizzbuzz(60)}"
    assert fizzbuzz(75) == "FizzBuzz", f"Expected 'FizzBuzz' for 75, got {fizzbuzz(75)}"
    assert fizzbuzz(90) == "FizzBuzz", f"Expected 'FizzBuzz' for 90, got {fizzbuzz(90)}"

    # Plain numbers (not divisible by 3 or 5)
    assert fizzbuzz(1) == 1, f"Expected 1 for 1, got {fizzbuzz(1)}"
    assert fizzbuzz(2) == 2, f"Expected 2 for 2, got {fizzbuzz(2)}"
    assert fizzbuzz(4) == 4, f"Expected 4 for 4, got {fizzbuzz(4)}"
    assert fizzbuzz(7) == 7, f"Expected 7 for 7, got {fizzbuzz(7)}"
    assert fizzbuzz(8) == 8, f"Expected 8 for 8, got {fizzbuzz(8)}"
    assert fizzbuzz(11) == 11, f"Expected 11 for 11, got {fizzbuzz(11)}"
    assert fizzbuzz(13) == 13, f"Expected 13 for 13, got {fizzbuzz(13)}"
    assert fizzbuzz(97) == 97, f"Expected 97 for 97, got {fizzbuzz(97)}"
    assert fizzbuzz(100) == 100, f"Expected 100 for 100, got {fizzbuzz(100)}"

    print("All tests passed!")


if __name__ == "__main__":
    # Run the test suite first to verify correctness
    run_tests()
    print()
    # Then run the FizzBuzz logic for numbers 1-100
    run_fizzbuzz(1, 100)
