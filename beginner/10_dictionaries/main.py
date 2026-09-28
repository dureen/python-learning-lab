"""
Beginner Lesson 10 – Dictionaries
"""

def main() -> None:
    person = {
        "name": "Bob",
        "age": 30,
        "city": "Jakarta",
    }

    print(person["name"])
    person["age"] = 31
    person["job"] = "Developer"
    print(person)

    for key, value in person.items():
        print(f"{key}: {value}")

    # Dict comprehension
    squares = {x: x * x for x in range(1, 6)}
    print(squares)


if __name__ == "__main__":
    main()
