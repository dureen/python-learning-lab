"""
Advanced Lesson 10 – Simple Performance Tips
"""

import timeit


def list_comp() -> list[int]:
    return [x * x for x in range(1000)]


def for_loop() -> list[int]:
    result = []
    for x in range(1000):
        result.append(x * x)
    return result


def main() -> None:
    t1 = timeit.timeit(list_comp, number=1000)
    t2 = timeit.timeit(for_loop, number=1000)
    print(f"List comprehension: {t1:.4f}s")
    print(f"For loop:           {t2:.4f}s")


if __name__ == "__main__":
    main()
