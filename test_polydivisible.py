from polydivisible import Polydivisible


def test_base_four():
    """The base 4 polydivisible numbers with all digits are 123 and 321."""
    polydivisible = Polydivisible(base=4)
    assert set(polydivisible.search()) == {(1, 2, 3), (3, 2, 1)}


def test_base_five():
    """There are no base 5 polydivisible numbers using all digits."""
    polydivisible = Polydivisible(base=5)
    assert set(polydivisible.search()) == set()
