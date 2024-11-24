# Back to the Bank

from bank import value

# testing variations of the word "hello"
def test_hello():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("hEllO") == 0
    assert value("Hello, dear ...") == 0

# testing variations of greetings starting with "h"
def test_h():
    assert value("Hej") == 20
    assert value("hej") == 20
    assert value("Hi") == 20
    assert value("Hej, dear customer") == 20

# testing variations of greetings not starting with "h"
def test_other_greetings():
    assert value("Welcome") == 100
    assert value("welcome") == 100
    assert value("wElcOmE") == 100
    assert value("Good day to you") == 100
    assert value("Welcome, dear user") == 100