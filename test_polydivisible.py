from polydivisible import Polydivisible


def test_base_four():
    """The base 4 polydivisible numbers with all digits are 123 and 321."""
    polydivisible = Polydivisible(base=4)
    assert polydivisible.as_set() == {(1, 2, 3), (3, 2, 1)}


def test_base_five():
    """There are no base 5 polydivisible numbers using all digits."""
    polydivisible = Polydivisible(base=5)
    assert polydivisible.as_set() == set()


def test_as_list():
    """The as_list method returns a list of polydivisible sequences."""
    polydivisible = Polydivisible(base=10)
    assert polydivisible.as_list() == [(3, 8, 1, 6, 5, 4, 7, 2, 9)]


def test_as_set():
    """The as_set method returns a set of polydivisible sequences."""
    polydivisible = Polydivisible(base=8)
    assert polydivisible.as_set() == {
        (3, 2, 5, 4, 1, 6, 7),
        (5, 2, 3, 4, 7, 6, 1),
        (5, 6, 7, 4, 3, 2, 1),
    }
