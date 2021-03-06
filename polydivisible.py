from collections import Counter, defaultdict
from fractions import gcd


def coroutine(func):
    """Start a coroutine when first called."""
    def start(*args, **kwargs):
        """Call the coroutine `func` and call `next` on it to start."""
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start


def greatest_common_divisors(base):
    """Partition digits by their greatest common divisor with base."""
    factors = defaultdict(set)
    for i in range(1, base):
        factors[gcd(i, base)].add(i)
    return factors


class Polydivisible:
    def __init__(self, base, debug=False):
        self.base = base
        self.factors = greatest_common_divisors(base)
        self.debug = debug
        self._count = self.count_terminating_sequences()

    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, value):
        self._debug = value
        self.counter = Counter()

    def search(self, current_sequence=None, number=None):
        """
        Find all polydivisible numbers using all digits in the given base.

        A number is polydivisible in base `b` if the first `n` digits of the
        number are divisible by `n` for `n` in `range(1, b)`.

        We use a recursive backtracking algorithm to search the possibilities.
        """

        if current_sequence is None:
            if self.base % 2:  # Odd bases cannot have polydivisible numbers
                return

            for digit in self.factors[1]:
                # Start our search with sequences of one digit
                yield from self.search((digit,), digit)
            return  # We've found all possible polydivisible numbers

        next_divisor = len(current_sequence) + 1
        if next_divisor == self.base:
            # We've found a polydivisible number, so yield it and return
            yield current_sequence
            if self.debug:
                self._count.send(next_divisor)
            return

        number *= self.base
        # Extend our current_sequence with an available digit and continue search
        for digit in self.factors[gcd(next_divisor, self.base)]:
            if digit in current_sequence:
                continue
            next_number = number + digit
            if next_number % next_divisor == 0:
                yield from self.search(current_sequence + (digit,), next_number)
            elif self.debug:
                self._count.send(next_divisor)

    def as_list(self):
        """Return a list of all polydivisible sequences."""
        return list(self.search())

    def as_set(self):
        """Return a set of all polydivisible sequences."""
        return set(self.search())

    @coroutine
    def count_terminating_sequences(self):
        while True:
            sequence_length = yield
            self.counter[sequence_length] += 1


if __name__ == '__main__':  # pragma: nocover
    for base in range(2, 41):
        poly = Polydivisible(base)
        print(base, poly.as_list())
