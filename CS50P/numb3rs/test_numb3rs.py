from numb3rs import validate
import pytest

def test():
    assert validate("255.255.255.255") == True
    assert validate("255.010.001.001") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate ('1') == False
    assert validate ('....') == False
    assert validate("cat") == False
    assert validate('101.512.511.322') ==False
