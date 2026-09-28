"""
Intermediate Lesson 09 – Regular Expressions
"""

import re


def main() -> None:
    text = "Contact us at support@example.com or sales@company.org"

    emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)
    print("Emails found:", emails)

    # Substitution
    cleaned = re.sub(r"\s+", " ", "Too   many    spaces")
    print(cleaned)


if __name__ == "__main__":
    main()
