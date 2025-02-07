from src.Math_Utils import MathUtils

"""adding each method"""
def test_add():
    assert MathUtils.add(7, 3) == 10
    assert MathUtils.add(-9, 9) == 0
    assert MathUtils.add(0, 0) == 0

def test_subtract():
    assert MathUtils.subtract(3, 2) == 1
    assert MathUtils.subtract(2, 3) == -1
    assert MathUtils.subtract(0, 0) == 0

def test_multiply():
    assert MathUtils.multiply(3, 3) == 9
    assert MathUtils.multiply(-1, 1) == -1
    assert MathUtils.multiply(0, 5) == 0

def test_divide():
    assert MathUtils.divide(4, 2) == 2
    assert MathUtils.divide(5, 2) == 2.5
    assert MathUtils.divide(0, 1) == 0
    assert MathUtils.divide(1, 0) == -1 #Dividing by zero should return -1.0