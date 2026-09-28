"""
Beginner Lesson 02 – Variables
"""

def main() -> None:
    name = "Alice"
    age = 25
    height = 1.68
    is_student = True

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Height: {height} m")
    print(f"Is student: {is_student}")

    # Reassignment
    age = 26
    print(f"New age: {age}")


if __name__ == "__main__":
    main()
