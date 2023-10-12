from working import convert
import pytest

def test_convert():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    with pytest.raises(ValueError):
         convert('12:00 AM - 12:00 PM')
    with pytest.raises(ValueError):
         convert('12:00AM to 12:00PM')
    with pytest.raises(ValueError):
         convert('09:10 AM to 24:00 PM')
    with pytest.raises(ValueError):
         convert('9:60 AM to 5:60 PM')
