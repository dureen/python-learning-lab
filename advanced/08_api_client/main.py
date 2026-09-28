"""
Advanced Lesson 08 – Simple API Client (using urllib)
"""

import json
from urllib.request import urlopen


def fetch_json(url: str) -> dict:
    with urlopen(url) as response:
        return json.loads(response.read().decode())


def main() -> None:
    # Public free API example
    data = fetch_json("https://httpbin.org/get")
    print("URL:", data.get("url"))
    print("Origin:", data.get("origin"))


if __name__ == "__main__":
    main()
