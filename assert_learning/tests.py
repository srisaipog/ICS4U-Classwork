import functions

def test_add():
    assert functions.add(1, 5, 6) == 12
    assert functions.add(420, 68) == 488

def test_cool():
    assert functions.name_is_cool("Sridhar") == "Sridhar is cool :)"
    assert functions.name_is_cool("(: cool is") == "(: cool is is cool :)"

def test_blip():
    assert functions.blip_blop("My life is a lie") == "blip blop blip blop blip"
    assert functions.blip_blop("die potato die") == "blip blop blip"