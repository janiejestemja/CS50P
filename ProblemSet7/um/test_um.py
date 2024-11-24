from um import count

def test_count_a():
    # testing punctuation
    assert count("Um?") == 1
    assert count("hello, um, world.") == 1
    assert count("Um, hello, um, world.") == 2
    assert count("Um, thanks, um...") == 2

def test_count_b():
    # testing lower and upper case
    assert count("um") == 1
    assert count("UM") == 1
    assert count("uM") == 1
    assert count("Um") == 1

def test_count_c():
    # testing cornercases
    assert count("yummy") == 0
    assert count("yu um my") == 1
    assert count("circumstance") == 0 
    assert count("circ_um_stance") == 0