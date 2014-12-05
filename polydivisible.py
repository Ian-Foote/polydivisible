from collections import defaultdict
from fractions import gcd
from functools import lru_cache
import itertools


@lru_cache()
def mask(base, divisor):
    return list(reversed([pow(base, power, divisor) for power in range(divisor)]))


def divisible(sequence, base):
    """Check if a sequence is divisible by its length in the given base."""
    divisor = len(sequence)
    if base % divisor == 0:
        return sequence[-1] % divisor == 0

    components = (digit * r for digit, r in zip(sequence, mask(base, divisor)))
    return sum(components) % divisor == 0


def greatest_common_divisors(base):
    """Partition digits by their greatest common divisor with base."""
    factors = defaultdict(set)
    for i in range(1, base):
        factors[gcd(i, base)].add(i)
    return factors


def search(base, current_sequence=None, factors=None):
    """
    Find all polydivisible numbers using all digits in the given base.

    A number is polydivisible in base `b` if the first `n` digits of the
    number are divisible by `n` for `n` in `range(1, b)`.

    We use a recursive backtracking algorithm to search the possibilities.
    """
    if factors is None:
        factors = greatest_common_divisors(base)

    if current_sequence is None:
        for digit in factors[1]:
            # Start our search with sequences of one digit
            yield from search(base, (digit,), factors)
        return  # We've found all possible polydivisible numbers

    if not divisible(current_sequence, base):
        return

    next_divisor = len(current_sequence) + 1
    if next_divisor == base:
        # We've found a polydivisible number, so yield it and return
        yield current_sequence
        return

    # Extend our current_sequence with an available digit and continue search
    for digit in factors[gcd(next_divisor, base)]:
        if digit in current_sequence:
            continue
        yield from search(base, current_sequence + (digit,), factors)


if __name__ == '__main__':
    for base in range(2, 21):
        print(base, list(search(base)))
