from numb3rs import validate

def test_validate_true():
    # testing upper and lower bounds
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("256.255.255.255") == False
    assert validate("255.256.255.255") == False
    assert validate("255.255.256.255") == False
    assert validate("255.255.255.256") == False


def test_validate_false():
    # testing str instead of numbers
    assert validate("cat") == False
    assert validate("cat.dog.horse.lion") == False 

    # testing lengths
    assert validate("0") == False 
    assert validate("0.0") == False 
    assert validate("0.0.0") == False 
    assert validate("0.0.0.0.0") == False 
    
