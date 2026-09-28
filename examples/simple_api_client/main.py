"""Simple API client example using urllib."""

import json
from urllib.request import urlopen

def get_ip_info() -> dict:
    with urlopen("https://httpbin.org/ip") as resp:
        return json.loads(resp.read().decode())

def main() -> None:
    info = get_ip_info()
    print("Your origin IP (via httpbin):", info.get("origin"))

if __name__ == "__main__":
    main()
