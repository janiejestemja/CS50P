import pytest
from working import convert

def test_convert_a():
    # checking usual cases
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"

def test_convert_b():
    # checking cornercases and capitalization
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 am to 12 PM") == "00:00 to 12:00"
    assert convert("12 AM to 12 pm") == "00:00 to 12:00"
    assert convert("12 am to 12 pm") == "00:00 to 12:00"
    assert convert("12 aM to 12 Pm") == "00:00 to 12:00"

def test_convert_c():
    # testing exceptions
    with pytest.raises(ValueError):
        convert("cat")
        convert("12:60 am to 11:60 pm")
        convert("13:15 am to 14:15 pm")
        convert("1315 am to 5 pm")


