"""Tests for surjective_counting.py"""

from surjective_counting import surject1, surject2


def test_counting():
    """tests if the two implementations compute the same"""
    for m in range(15):
        for n in range(m + 2):
            assert surject1(m, n) == surject2(m, n)
