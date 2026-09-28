"""Tests for advanced testing lesson."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "advanced" / "07_testing"))

from main import is_palindrome


def test_palindrome_true():
    assert is_palindrome("A man a plan a canal Panama") is True


def test_palindrome_false():
    assert is_palindrome("hello") is False
