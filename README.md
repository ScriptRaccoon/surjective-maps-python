# Listing and counting surjective maps between finite sets

A function `f : X -> Y` is surjective when every element of `Y` is hit by at least one element in `X` by means of `f`. When `X` and `Y` are finite sets, these functions can be seen as tuples, and surjectivity means that every element appears at least once in the tuple.

There are at least two ways to _count_ the surjective tuples. In `surjective_counting.py` the performance of the two methods are compared. There are also several methods to _list_ all of the surjective tuples, their performance is compared in `surjective_tuples.py`.
