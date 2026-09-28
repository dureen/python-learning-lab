"""
Advanced Lesson 05 – Advanced OOP (inheritance, properties, dunder methods)
"""

class Animal:
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def speak(self) -> str:
        raise NotImplementedError


class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says meow"

    def __repr__(self) -> str:
        return f"Cat(name={self.name!r})"


def main() -> None:
    cat = Cat("Whiskers")
    print(cat)
    print(cat.speak())


if __name__ == "__main__":
    main()
