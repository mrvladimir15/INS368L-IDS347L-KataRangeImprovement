import pytest
from main import getFI
from main import getFN
from main import getLN
from main import getLI
from main import Range

def test_getFI():
    assert getFI("(2,7)") == '('
    
def test_getFN():
    assert getFN("(2,7)") == 2
    
def test_getLN():
    assert getLN("(2,7)") == 7
    
def test_getLI():
    assert getLI("(2,6]") == ']'

class testRange():
    interval="(2,7]"
    
    def test_getEquals(self):
        assert Range.getEquals(self,"[3,8)") == True
    def getAllpoints(self):
        assert range.getAllpoints(self) == ("3","4","5","6","7")