"""Tests for surjective_tuples.py"""

# pylint: disable=missing-function-docstring

from surjective_tuples import (
    surjective_tuples,
    surjective_tuples_kelly,
    surjective_tuples_stupid,
)


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


def test_agree():
    for m in range(5):
        for n in range(5):
            res1 = surjective_tuples(m, n)
            res2 = surjective_tuples_kelly(m, n)
            res3 = surjective_tuples_stupid(m, n)
            assert res1 == set(res2) == set(res3)
