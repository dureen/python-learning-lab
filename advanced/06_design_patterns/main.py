"""
Advanced Lesson 06 – Design Patterns (Singleton & Factory simple examples)
"""

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


def create_shape(kind: str):
    if kind == "circle":
        return {"type": "circle", "area": lambda r: 3.14 * r * r}
    if kind == "square":
        return {"type": "square", "area": lambda s: s * s}
    raise ValueError(f"Unknown shape: {kind}")


def main() -> None:
    a = Singleton()
    b = Singleton()
    print(a is b)  # True

    circle = create_shape("circle")
    print(circle["area"](5))


if __name__ == "__main__":
    main()
