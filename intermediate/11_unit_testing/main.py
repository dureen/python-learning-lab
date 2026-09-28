"""
Intermediate Lesson 11 – Unit Testing (example functions)
"""

def add(a: int, b: int) -> int:
    return a + b


def is_even(n: int) -> bool:
    return n % 2 == 0


if __name__ == "__main__":
    print(add(2, 3))
    print(is_even(4))
