import polydivisible


def test_base_four():
    """The base 4 polydivisible numbers with all digits are 123 and 321."""
    assert set(polydivisible.search(base=4)) == {(1, 2, 3), (3, 2, 1)}


def test_base_five():
    """There are no base 5 polydivisible numbers using all digits."""
    assert set(polydivisible.search(base=5)) == set()
