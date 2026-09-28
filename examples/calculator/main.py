"""Simple calculator example."""

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main() -> None:
    print("Calculator")
    print("2 + 3 =", add(2, 3))
    print("10 / 2 =", divide(10, 2))

if __name__ == "__main__":
    main()
