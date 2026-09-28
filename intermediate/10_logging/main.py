"""
Intermediate Lesson 10 – Logging
"""

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

logger = logging.getLogger(__name__)


def main() -> None:
    logger.debug("This is a debug message")
    logger.info("Application started")
    logger.warning("Something looks suspicious")
    logger.error("An error occurred")


if __name__ == "__main__":
    main()
