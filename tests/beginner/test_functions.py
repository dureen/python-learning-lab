"""Tests for beginner functions lesson."""

import sys
from pathlib import Path

# Add lesson to path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "beginner" / "08_functions"))

from main import greet, add


def test_greet_default():
    assert greet() == "Hello, World!"


def test_greet_name():
    assert greet("Python") == "Hello, Python!"


def test_add():
    assert add(2, 3) == 5
