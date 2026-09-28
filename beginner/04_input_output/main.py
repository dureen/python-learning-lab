"""
Beginner Lesson 04 – Input & Output
"""

def main() -> None:
    name = input("What is your name? ")
    age = int(input("How old are you? "))

    print(f"Hello, {name}! Next year you will be {age + 1}.")


if __name__ == "__main__":
    main()
