from numb3rs import validate

def test_validate_true():
    # testing upper and lower bounds
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

    # testing every location in the adress
    for i in range(256):
        assert validate(f"{i}.0.0.0") == True
        assert validate(f"0.{i}.0.0") == True
        assert validate(f"0.0.{i}.0") == True
        assert validate(f"0.0.0.{i}") == True

def test_validate_false():
    # testing str instead of numbers
    assert validate("cat") == False
    assert validate("cat.dog.horse.lion") == False 

    # testing lengths
    assert validate("0") == False 
    assert validate("0.0") == False 
    assert validate("0.0.0") == False 
    assert validate("0.0.0.0.0") == False 
    