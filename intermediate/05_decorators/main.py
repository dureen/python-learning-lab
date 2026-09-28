"""
Intermediate Lesson 05 – Decorators
"""

import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f}s")
        return result
    return wrapper


@timer
def slow_add(a: int, b: int) -> int:
    time.sleep(0.1)
    return a + b


def main() -> None:
    print(slow_add(3, 4))


if __name__ == "__main__":
    main()
