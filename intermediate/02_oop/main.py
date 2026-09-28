"""
Intermediate Lesson 02 – Object-Oriented Programming
"""

class Dog:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def bark(self) -> str:
        return f"{self.name} says woof!"

    def __str__(self) -> str:
        return f"Dog(name={self.name}, age={self.age})"


def main() -> None:
    dog = Dog("Buddy", 3)
    print(dog)
    print(dog.bark())


if __name__ == "__main__":
    main()
