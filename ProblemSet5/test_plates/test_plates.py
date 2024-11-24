# Re-requesting a Vanity Plate

from plates import is_valid

# testing length-check
def test_length():
    assert is_valid("") == False 
    assert is_valid("A") == False
    assert is_valid("AA") == True
    assert is_valid("AAA") == True 
    assert is_valid("AAAA") == True 
    assert is_valid("AAAAA") == True 
    assert is_valid("AAAAAA") == True 
    assert is_valid("AAAAAAA") == False 

# testing first two letters-check
def test_letters():
    for i in range(97, 123):
        assert is_valid(chr(i)*6) == True 

# testing numbers-check and first-number-check
def test_numbers():
    assert is_valid("123456") == False
    assert is_valid("A23456") == False
    assert is_valid("AB1234") == True
    assert is_valid("AB34EF") == False
    assert is_valid("ABC45F") == False
    assert is_valid("ABCD56") == True 
    assert is_valid("AB0123") == False

# testing puncuation
def test_punctuation():
    assert is_valid("AB-DE-") == False 
    assert is_valid("AB_D_F") == False
    assert is_valid("HELLO!") == False