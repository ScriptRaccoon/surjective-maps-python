"""Tests for surjective_tuples.py"""

from surjective_tuples import surjective_tuples


def test_2_0():
    assert surjective_tuples(2, 0) == set()


def test_2_3():
    assert surjective_tuples(2, 3) == set()


def test_2_2():
    assert surjective_tuples(2, 2) == {(0, 1), (1, 0)}


def test_4_3():
    assert surjective_tuples(4, 3) == {
        (2, 1, 0, 0),
        (2, 0, 1, 0),
        (2, 0, 0, 1),
        (2, 1, 1, 0),
        (2, 1, 0, 1),
        (2, 0, 1, 1),
        (1, 2, 0, 0),
        (0, 2, 1, 0),
        (0, 2, 0, 1),
        (1, 2, 1, 0),
        (1, 2, 0, 1),
        (0, 2, 1, 1),
        (1, 0, 2, 0),
        (0, 1, 2, 0),
        (0, 0, 2, 1),
        (1, 1, 2, 0),
        (1, 0, 2, 1),
        (0, 1, 2, 1),
        (1, 0, 0, 2),
        (0, 1, 0, 2),
        (0, 0, 1, 2),
        (1, 1, 0, 2),
        (1, 0, 1, 2),
        (0, 1, 1, 2),
        (2, 2, 1, 0),
        (2, 2, 0, 1),
        (2, 1, 2, 0),
        (2, 0, 2, 1),
        (2, 1, 0, 2),
        (2, 0, 1, 2),
        (1, 2, 2, 0),
        (0, 2, 2, 1),
        (1, 2, 0, 2),
        (0, 2, 1, 2),
        (1, 0, 2, 2),
        (0, 1, 2, 2),
    }
