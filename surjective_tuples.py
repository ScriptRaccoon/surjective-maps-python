# https://stackoverflow.com/questions/77379001/efficient-computation-of-the-set-of-surjective-functions


"""Compute the list of all surjective maps between two finite sets,
encoded as m-tuples of numbers < n where every number < n appears
at least once. The implementation below is recursive. For example,
consider the tuple

(1,6,4,2,1,6,0,2,5,1,3,2,3)

in which every number < 7 appears at least once. Look at the largest
number and erase it:

(1,*,4,2,1,*,0,2,5,1,3,2,3)

It appears in the indices 1 and 5, so this corresponds to the set {1,5}.
The rest corresponds to the tuple

(1,4,2,1,0,2,5,1,3,2,3)

with the same restriction that every number < 6 appears at least once.

So, the list of surjective m-tuples of numbers < n corresponds to the pairs
(T,a), where T is a non-empty subset of {0,...,m-1} and a is a surjective
(m-k)-tuple of numbers < n-1, where T has k elements. This is a recursive
description and will be implemented below.
"""

import itertools
from time import perf_counter


# my version
def surjective_tuples(m: int, n: int) -> set[tuple]:
    """Set of all m-tuples of numbers < n where every number < n appears at least once.

    Arguments:
        m: length of the tuple
        n: number of distinct values
    """
    if n == 0:
        return set() if m > 0 else {()}
    if n > m:
        return set()
    result = set()
    for k in range(1, m + 1):
        smaller_tuples = surjective_tuples(m - k, n - 1)
        subsets = itertools.combinations(range(m), k)
        for subset in subsets:
            for smaller_tuple in smaller_tuples:
                my_tuple = []
                count = 0
                for i in range(m):
                    if i in subset:
                        my_tuple.append(n - 1)
                        count += 1
                    else:
                        my_tuple.append(smaller_tuple[i - count])
                result.add(tuple(my_tuple))
    return result


# written by Kelly, runs faster
def surjective_tuples2(m: int, n: int) -> list[tuple]:
    """List of all m-tuples of numbers < n where every number < n appears at least once.

    Arguments:
        m: length of the tuple
        n: number of distinct values
    """
    if not n:
        return [] if m else [()]
    if n > m:
        return []
    n -= 1
    result = []
    for k in range(1, m - n + 1):
        smaller_tuples = surjective_tuples(m - k, n)
        subsets = itertools.combinations(range(m), k)
        for subset in subsets:
            for smaller_tuple in smaller_tuples:
                my_tuple = [*smaller_tuple]
                for i in subset:
                    my_tuple.insert(i, n)
                result.append(tuple(my_tuple))
    return result


def surjective_tuples_stupid(m: int, n: int) -> list[int]:
    """List of all m-tuples of numbers < n where every number < n appears at least once.
    Implemented as stupidly as possible by filtering out the surjective tuples
    within all tuples.

    Arguments:
        m: length of the tuple
        n: number of distinct values
    """
    all_tuples = list(itertools.product(*(range(n) for _ in range(m))))
    surjective_tuples = filter(lambda t: all(i in t for i in range(n)), all_tuples)
    return list(surjective_tuples)


if __name__ == "__main__":
    m, n = 9, 6
    start1 = perf_counter()
    res1 = surjective_tuples(m, n)
    end1 = perf_counter()
    time1 = end1 - start1
    print(time1)

    start2 = perf_counter()
    res2 = surjective_tuples2(m, n)
    end2 = perf_counter()
    time2 = end2 - start2
    print(time2)

    assert res1 == set(res2)

    start3 = perf_counter()
    res3 = surjective_tuples_stupid(m, n)
    end3 = perf_counter()
    time3 = end3 - start3
    print(time3)

    assert set(res3) == set(res2)
