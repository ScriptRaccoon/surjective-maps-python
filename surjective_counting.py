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
    if not n:
        return int(m == 0)
    return sum(comb(m, k) * surject1(k, n - 1) for k in range(m))


# winner
def surject2(m: int, n: int) -> int:
    """number of surjective maps [m] -> [n] where [n] is a set
    with n elements, counted with inclusion-exclusion principle"""
    if n > m:
        return 0
    if not m:
        return 1
    return sum((-1) ** i * comb(n, i) * (n - i) ** m for i in range(n))


if __name__ == "__main__":
    values = [(10, 5), (10, 2), (20, 1), (20, 10), (20, 15), (20, 20)]
    for m, n in values:
        print("recursive implemention")
        start1 = perf_counter()
        surject1(m, n)
        end1 = perf_counter()
        time1 = end1 - start1
        print(f"{m},{n}: {time1}")
        print("inclusion-exclusion implemention")
        start2 = perf_counter()
        surject2(m, n)
        end2 = perf_counter()
        time2 = end2 - start2
        print(f"{m},{n}: {time2}")
        print("ratio=", time1 / time2)
        print()
