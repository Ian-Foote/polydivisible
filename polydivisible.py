import itertools


def sequence_to_integer(sequence, base):
    """Convert a sequence of digits into an integer using the given base."""
    num_digits = len(sequence)
    exponents = reversed(range(num_digits))
    powers = (base ** exponent for exponent in exponents)
    return sum(digit * power for digit, power in zip(sequence, powers))


def search(base):
    """
    Find all polydivisible numbers using all digits in the given base.

    A number is polydivisible in base `b` if the first `n` digits of the
    number are divisible by `n` for `n` in `range(1, b)`.
    """

    for digit_sequence in itertools.permutations(range(1, base)):
        for divisor in range(2, base):
            subsequence = digit_sequence[:divisor]
            number = sequence_to_integer(subsequence, base=base)
            if number % divisor:
                break
        else:
            yield digit_sequence
