from jar import Jar
import pytest

def test1():
    with pytest.raises(ValueError):
        jar = Jar(-114514)

def test2():
    jar = Jar()
    assert str(jar) == ''
    jar.deposit(1)
    assert str(jar) == '🍪'
    with pytest.raises(ValueError):
        jar.deposit(114514)

def test3():
    jar = Jar()
    jar.deposit(2)
    assert str(jar) == '🍪🍪'
    jar.withdraw(1)
    assert str(jar) == '🍪'
    
def test4():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(114514)
