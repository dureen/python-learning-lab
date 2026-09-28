"""
Advanced Lesson 04 – Multiprocessing
"""

from multiprocessing import Process, Queue
import time


def worker(name: str, q: Queue) -> None:
    time.sleep(0.5)
    q.put(f"Result from {name}")


def main() -> None:
    q: Queue = Queue()
    processes = [
        Process(target=worker, args=("Proc-A", q)),
        Process(target=worker, args=("Proc-B", q)),
    ]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    while not q.empty():
        print(q.get())


if __name__ == "__main__":
    main()
