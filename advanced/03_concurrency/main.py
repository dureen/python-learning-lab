"""
Advanced Lesson 03 – Concurrency (threading)
"""

import threading
import time


def worker(name: str, delay: float) -> None:
    print(f"{name} starting")
    time.sleep(delay)
    print(f"{name} finished")


def main() -> None:
    threads = [
        threading.Thread(target=worker, args=("Thread-A", 1.0)),
        threading.Thread(target=worker, args=("Thread-B", 0.5)),
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("All done")


if __name__ == "__main__":
    main()
