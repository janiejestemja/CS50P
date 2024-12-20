import pytest
from working import convert

def test_convert():
    # checking usual cases
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

    # testing exceptions
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("12:60 AM to 11:60 PM")
    with pytest.raises(ValueError):
        convert("13:15 AM to 14:15 PM")
    with pytest.raises(ValueError):
        convert("1315 AM to 5 AM")


