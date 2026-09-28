"""Tests for intermediate OOP lesson."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "intermediate" / "02_oop"))

from main import Dog


def test_dog_bark():
    dog = Dog("Rex", 2)
    assert dog.bark() == "Rex says woof!"


def test_dog_str():
    dog = Dog("Rex", 2)
    assert "Rex" in str(dog)
