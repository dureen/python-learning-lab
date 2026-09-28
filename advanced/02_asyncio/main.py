"""
Advanced Lesson 02 – Asyncio
"""

import asyncio


async def fetch_data(name: str, delay: float) -> str:
    print(f"Fetching {name}...")
    await asyncio.sleep(delay)
    return f"Data from {name}"


async def main() -> None:
    results = await asyncio.gather(
        fetch_data("API-A", 1.0),
        fetch_data("API-B", 0.5),
        fetch_data("API-C", 0.8),
    )
    for r in results:
        print(r)


if __name__ == "__main__":
    asyncio.run(main())
