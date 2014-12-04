import itertools


def sequence_to_integer(sequence, base):
    """Convert a sequence of digits into an integer using the given base."""
    num_digits = len(sequence)
    exponents = reversed(range(num_digits))
    powers = (base ** exponent for exponent in exponents)
    return sum(digit * power for digit, power in zip(sequence, powers))


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

    divisor = len(current_sequence)
    number = sequence_to_integer(current_sequence, base)
    if number % divisor:
        return  # The current_sequence is not polydivisible

    if divisor == base - 1:
        # We've found a polydivisible number, so yield it and return
        yield current_sequence
        return

    # Extend our current_sequence with an available digit and continue search
    for digit in range(1, base):
        if digit in current_sequence:
            continue
        yield from search(base, current_sequence + (digit,))


if __name__ == '__main__':
    for base in range(21):
        print(base, list(search(base)))
