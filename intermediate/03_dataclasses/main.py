"""
Intermediate Lesson 03 – Dataclasses
"""

from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    price: float
    tags: list[str] = field(default_factory=list)

    def apply_discount(self, percent: float) -> float:
        return self.price * (1 - percent / 100)


def main() -> None:
    p = Product("Laptop", 1200.0, ["electronics", "computer"])
    print(p)
    print(f"Discounted: {p.apply_discount(10):.2f}")


if __name__ == "__main__":
    main()
