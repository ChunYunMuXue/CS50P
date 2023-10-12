from um import count

def test():
    assert count('um umumumuuum') == 1
    assert count('um, can i... um... help?') == 2
    assert count('umumumuuum') == 0
    assert count('mum ') == 0
    assert count(' um ') == 1
    assert count('UM') == 1
    assert count('?um UM Um uM uuum') == 4
