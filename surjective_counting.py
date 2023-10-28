"""
Performance comparison of two implementations of the function that
counts the surjective maps between two finite sets.
"""


from math import comb
from time import perf_counter


# looser
def surject1(m: int, n: int) -> int:
    """number of surjective maps [m] -> [n] where [n] is a set
    with n elements, recursive implementation"""
    if n == 0:
        return int(m == 0)
    return sum(comb(m, k) * surject1(k, n - 1) for k in range(m))


# winner
def surject2(m: int, n: int) -> int:
    """number of surjective maps [m] -> [n] where [n] is a set
    with n elements, counted with inclusion-exclusion principle"""
    if n > m:
        return 0
    if m == 0:
        return 1
    return sum((-1) ** i * comb(n, i) * (n - i) ** m for i in range(n))


def test_equality(limit: int = 15) -> None:
    """tests if the two implementations compute the same"""
    print("Test if the two implementations compute the same")
    for m in range(limit):
        for n in range(m):
            assert surject1(m, n) == surject2(m, n)
    print("OK")


def measure_fun(fun, msg="") -> None:
    """measures performance of a function"""
    print(msg)
    values = [(10, 5), (10, 2), (20, 10), (20, 20), (20, 1), (25, 25)]
    for m, n in values:
        start = perf_counter()
        fun(m, n)
        end = perf_counter()
        time = end - start
        print(m, n, ": ", time)


def main() -> None:
    """measure performance of the two implementations"""
    test_equality()
    measure_fun(surject1, msg="Test recursive implementation")
    measure_fun(surject2, msg="Test inclusion-exclusion implementation")


if __name__ == "__main__":
    main()
