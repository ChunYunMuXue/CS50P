from seasons import did
import pytest

def test_did():
     with pytest.raises(TypeError):
         did(19-12-2004) == 'Invalid date'

