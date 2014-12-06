from collections import defaultdict
from fractions import gcd


def mask(base, divisor):
    return list(reversed([pow(base, power, divisor) for power in range(divisor)]))


def digit_weights(base):
    return {divisor: mask(base, divisor) for divisor in range(1, base)}


def greatest_common_divisors(base):
    """Partition digits by their greatest common divisor with base."""
    factors = defaultdict(set)
    for i in range(1, base):
        factors[gcd(i, base)].add(i)
    return factors


class Polydivisible:
    def __init__(self, base):
        self.base = base
        self.factors = greatest_common_divisors(base)
        self.digit_weights = digit_weights(base)

    def search(self, current_sequence=None):
        """
        Find all polydivisible numbers using all digits in the given base.

        A number is polydivisible in base `b` if the first `n` digits of the
        number are divisible by `n` for `n` in `range(1, b)`.

        We use a recursive backtracking algorithm to search the possibilities.
        """

        if current_sequence is None:
            for digit in self.factors[1]:
                # Start our search with sequences of one digit
                yield from self.search((digit,))
            return  # We've found all possible polydivisible numbers

        if not self.divisible(current_sequence):
            return

        next_divisor = len(current_sequence) + 1
        if next_divisor == self.base:
            # We've found a polydivisible number, so yield it and return
            yield current_sequence
            return

        # Extend our current_sequence with an available digit and continue search
        for digit in self.factors[gcd(next_divisor, self.base)]:
            if digit in current_sequence:
                continue
            yield from self.search(current_sequence + (digit,))

    def divisible(self, sequence):
        """Check if a sequence is divisible by its length in the given base."""
        divisor = len(sequence)
        if self.base % divisor == 0:
            return sequence[-1] % divisor == 0

        digit_powers = zip(sequence, self.digit_weights[divisor])
        components = (digit * r for digit, r in digit_powers)
        return sum(components) % divisor == 0


if __name__ == '__main__':  # pragma: nocover
    for base in range(2, 21):
        poly = Polydivisible(base)
        print(base, list(poly.search()))
