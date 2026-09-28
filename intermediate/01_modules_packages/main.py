"""
Intermediate Lesson 01 – Modules & Packages
"""

import math
from datetime import datetime
from collections import Counter


def main() -> None:
    print(math.sqrt(16))
    print(datetime.now().strftime("%Y-%m-%d %H:%M"))

    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    print(Counter(words))


if __name__ == "__main__":
    main()
