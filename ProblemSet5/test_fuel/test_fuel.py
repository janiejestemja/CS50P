# Refueling

import pytest
from fuel import convert, gauge

def test_convert():
    # testing exceptions
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("cat/dog")

    # testing assertions
    assert convert("0/100") == 0
    assert convert("25/100") == 25
    assert convert("50/100") == 50
    assert convert("75/100") == 75
    assert convert("100/100") == 100

def test_gauge():

    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"

    # testing cornvercases
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
