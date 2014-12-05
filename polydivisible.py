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


def search(base, current_sequence=None):
    """
    Find all polydivisible numbers using all digits in the given base.

    A number is polydivisible in base `b` if the first `n` digits of the
    number are divisible by `n` for `n` in `range(1, b)`.

    We use a recursive backtracking algorithm to search the possibilities.
    """

    if current_sequence is None:
        for digit in range(1, base):
            # Start our search with sequences of one digit
            yield from search(base, (digit,))
        return  # We've found all possible polydivisible numbers

    if not divisible(current_sequence, base):
        return

    if len(current_sequence) == base - 1:
        # We've found a polydivisible number, so yield it and return
        yield current_sequence
        return

    # Extend our current_sequence with an available digit and continue search
    for digit in range(1, base):
        if digit in current_sequence:
            continue
        yield from search(base, current_sequence + (digit,))


if __name__ == '__main__':
    for base in range(2, 21):
        print(base, list(search(base)))
