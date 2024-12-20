from seasons import func
from datetime import date
import pytest

def test_func():
    # testing common cases
    assert func(
        date(year=2000, month=1, day=2),
        date(year=2000, month=1, day=1),
    ) == "One thousand, four hundred forty minutes"

    assert func(
        date(year=2000, month=1, day=1),
        date(year=1999, month=1, day=1),
    ) == "Five hundred twenty-five thousand, six hundred minutes"
    
    # testing exceptions
    with pytest.raises(ValueError):
        func(
            date(year=2000, month=1, day=1),
            date(year=2000, month=1, day=2),
        )
