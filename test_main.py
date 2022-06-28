import pytest
from main import getFI
from main import getFN
from main import getLN
from main import getLI
from main import getEquals

def test_getFI():
    assert getFI("(2,7)") == '('
    
def test_getFN():
    assert getFN("(2,7)") == 2
    
def test_getLN():
    assert getLN("(2,7)") == 7
    
def test_getLI():
    assert getLI("(2,6]") == ']'
def test_getEquals():
    assert getEquals("(2,7]","[3,8)") == True 