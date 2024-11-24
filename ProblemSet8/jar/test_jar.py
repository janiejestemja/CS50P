from jar import Jar
import pytest


def test_init():
    # testing negative capacity 
    with pytest.raises(ValueError):
        jar = Jar(capacity=-1)
        jar.capacity = -1

def test_str():
    # instanciating object (Jar)
    jar = Jar()

    # testing __str__
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    # instanciating object (Jar)
    jar = Jar()

    # testing deposit and if size can match capacity
    assert jar.size == 0
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(10)
    assert jar.size == jar.capacity

    # reinitialising object
    jar = Jar()
    # testing exceptions
    with pytest.raises(ValueError):
        jar.deposit(-1)
        jar.deposit(13)


def test_withdraw():
    # instanciating object (Jar)
    jar = Jar()
    # filling the jar
    jar.deposit(12)

    # testing withdraw
    jar.withdraw(2) 
    assert jar.size == 10

    # testing emptying jar by withdrawing its current size
    jar.withdraw(jar.size) 
    assert jar.size == 0

    # testing exeptions
    with pytest.raises(ValueError):
        jar.withdraw(-1)
        jar.withdraw(1)
