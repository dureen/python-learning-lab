"""
Beginner Lesson 11 – Strings
"""

def main() -> None:
    text = "  Python Learning Lab  "
    print(text.strip())
    print(text.lower())
    print(text.upper())
    print(text.replace("Lab", "Repository"))

    words = "apple,banana,cherry".split(",")
    print(words)
    print("-".join(words))

    name = "Alice"
    print(f"Hello, {name}!")


if __name__ == "__main__":
    main()
