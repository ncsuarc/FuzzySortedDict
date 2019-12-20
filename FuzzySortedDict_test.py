from FuzzySortedDict import FuzzySortedDict
import pytest


def test_basic():
    fsd = FuzzySortedDict()

    with pytest.raises(KeyError):
        fsd[0]

    fsd[0] = "a"
    assert fsd[0] == "a"
    fsd[0] = "b"
    assert fsd[0] == "b"


def test_round_closest():
    fsd = FuzzySortedDict(rounding=0)

    fsd[0] = "a"
    fsd[3] = "b"
    assert fsd[-1] == "a"
    assert fsd[1] == "a"
    assert fsd[2] == "b"
    assert fsd[4] == "b"


def test_round_down():
    fsd = FuzzySortedDict(rounding=-1)

    fsd[0] = "a"
    fsd[3] = "b"
    with pytest.raises(KeyError):
        fsd[-1]
    assert fsd[1] == "a"
    assert fsd[2] == "a"
    assert fsd[4] == "b"


def test_round_up():
    fsd = FuzzySortedDict(rounding=1)

    fsd[0] = "a"
    fsd[3] = "b"
    assert fsd[-1] == "a"
    assert fsd[1] == "b"
    assert fsd[2] == "b"
    with pytest.raises(KeyError):
        fsd[4]
