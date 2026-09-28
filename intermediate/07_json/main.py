"""
Intermediate Lesson 07 – JSON
"""

import json
from pathlib import Path


def main() -> None:
    data = {
        "name": "Alice",
        "skills": ["Python", "Git"],
        "active": True,
    }

    # Serialize
    json_str = json.dumps(data, indent=2)
    print(json_str)

    # Write to file
    path = Path("data.json")
    path.write_text(json_str)

    # Read back
    loaded = json.loads(path.read_text())
    print(loaded)


if __name__ == "__main__":
    main()
