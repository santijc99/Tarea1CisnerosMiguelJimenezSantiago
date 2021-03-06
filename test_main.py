import pytest
from main import check_char
from main import caps_switch

#test de las funciones

@pytest.mark.parametrize( #tests para check_char
    "input_a,expected",[
    ("S",0),
    ("no",1),
    ("}",1),
    (5,1)]
    )
    
def test_check_char(input_a,expected):
    assert check_char(input_a)== expected

@pytest.mark.parametrize( #tests para check_char
    "input_a,expected",[
    ("S",0),]
    )
    
def test_caps_switch(input_a,expected):
    assert check_char(input_a)== expected    
    
