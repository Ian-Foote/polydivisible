# Proofs

## Odd bases have no polydivisible numbers

We can write any number as a sum:

![`d_n * b^n + ... + d_2 * b^2 + d_1 * b + d_0`](tex-images/odd-proof-1.png)

where `b` is the `base` and `n` is the index of the highest `digit`.

A polydivisible number has `base - 1` digits, and so `n` is `base - 2` (0-indexing).

From the definition of a polydivisible number, we know that it must be divisible by `base - 1`.

From the definition of divisibility a polydivisible number satisfies:

![`d_n * b^n + ... + d_2 * b^2 + d_1 * b + d_0 == 0 (mod b - 1)`](tex-images/odd-proof-2.png)

but we know that:

![`b == 1 (mod b - 1)`](tex-images/odd-proof-3.png)

so we can write:

![`d_n + ... + d_2 + d_1 + d_0 == 0 (mod b - 1)`](tex-images/odd-proof-4.png)

From the definition of polydivisible, we know that ![`d_0, ..., d_n`](tex-images/digits.png) are chosen uniquely from ![`1, 2, ..., b - 1`](tex-images/digit-choices.png). But there are exactly `base - 1` digits in both sets, so we can replace ![`d_0, ..., d_n`](tex-images/digits.png) with ![`1, 2, ..., b - 1`](tex-images/digit-choices.png):

![`1 + 2 + ... + b - 1 == 0 (mod b - 1)` `b(b - 1)/2 == 0 (mod b - 1)`](tex-images/odd-proof-5.png)

If `b` is odd, this factors as:

![`(b) * ((b - 1) / 2)`](tex-images/odd-proof-6.png)

`b` is coprime to `b - 1`, so is not divisible by `b - 1` or any of its factors. This means that `b - 1` must divide `(b - 1)/2` for the number to be polydivisible. This is a contradiction, so the `base` must not be odd.
