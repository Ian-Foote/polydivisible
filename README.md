polydivisible
=============

Search for polydivisible numbers using all nonzero digits exactly once.

Examples:

```python

>>> from polydivisible import Polydivisible
>>> base_10 = Polydivisible(base=10)
>>> base_10.as_list()
[(3, 8, 1, 6, 5, 4, 7, 2, 9)]
>>> base_14 = Polydivisible(base=14)
>>> base_14.as_list()
[(9, 12, 3, 10, 5, 4, 7, 6, 11, 8, 1, 2, 13)]
>>> base_8 = Polydivisible(base=8)
>>> base_8.as_list()
[(3, 2, 5, 4, 1, 6, 7), (5, 2, 3, 4, 7, 6, 1), (5, 6, 7, 4, 3, 2, 1)]
>>> base_6 = Polydivisible(base=6, debug=True)
>>> base_6.as_list()
[(1, 4, 3, 2, 5), (5, 4, 3, 2, 1)]
>>> base_6.counter
Counter({4: 2, 6: 2})

```
