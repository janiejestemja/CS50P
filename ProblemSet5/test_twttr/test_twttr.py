# Testing my twttr

from twttr import shorten

def test_shorten():
    # testing usual case
    assert shorten("twitter") == "twttr"
    # testing upper case
    assert shorten("sOmEthIng :)") == "smthng :)"
    # testing punctuation and numbers
    assert shorten("'October' 31, 1749") == "'ctbr' 31, 1749"