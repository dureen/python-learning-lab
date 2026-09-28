"""
Beginner Lesson 12 – Files
"""

from pathlib import Path


def main() -> None:
    path = Path("sample.txt")

    # Write
    path.write_text("Hello from Python Learning Lab!\nLine 2\n")

    # Read
    content = path.read_text()
    print("Content:")
    print(content)

    # Append
    with path.open("a") as f:
        f.write("Appended line\n")

    print("Updated content:")
    print(path.read_text())

    # Clean up (optional)
    # path.unlink()


if __name__ == "__main__":
    main()
