from fuel import convert, gauge
import pytest

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(2) == "2%"

def test_convert():
    assert convert("100/100") == 100
    assert convert("3/4") == 75
    assert convert("0/100") == 0
    assert convert("99/100") == 99
    with pytest.raises(ZeroDivisionError):
        convert("114514/0")
    with pytest.raises(ValueError):
        convert("cat/dog")



