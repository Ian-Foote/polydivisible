polydivisible
=============

Search for polydivisible numbers using all nonzero digits exactly once.

Examples:

```python
>>> from polydivisible import search
>>> list(search(base=10))
[(3, 8, 1, 6, 5, 4, 7, 2, 9)]
>>> list(search(base=14))
[(9, 12, 3, 10, 5, 4, 7, 6, 11, 8, 1, 2, 13)]
>>> list(search(base=8))
[(3, 2, 5, 4, 1, 6, 7), (5, 2, 3, 4, 7, 6, 1), (5, 6, 7, 4, 3, 2, 1)]
```
