from IntStack import *


def test1() -> None:
    s = IntStack(1)
    assert s._peek() == 1
    s._push(4)
    assert s._size() == 2
    assert s._peek() == 4
    assert s._pop() == 4
    assert s._peek() == 1
    
def test2() -> None:
    s = IntStack()
    assert s._size() == 0
    s._push(1), s._push(2), s._push(3), s._push(4)
    assert s._size() == 4
    assert s._peek() == 4
    assert s._pop() == 4
    assert s._pop() == 3
    assert s._pop() == 2
    assert s._pop() == 1
    assert s._pop() == None
    assert s._pop() == None

def test3() -> None:
    s = IntStack()
    for i in range(6):
        s._push(i)
        assert s._peek() == i
    for i in range(6):
        s._pop()
    assert s._peek() == None