import pytest
import exc_02_07_factorial

def test_factorial_of_zero():
    expectedResult = 1
    result = exc_02_07_factorial.getFactorial(0)
    
    assert result == expectedResult
    
def test_factorial_of_five():
    expectedResult = 120
    result = exc_02_07_factorial.getFactorial(5)
    
    assert result == expectedResult
    
def test_factorial_of_six():
    expectedResult = 720
    result = exc_02_07_factorial.getFactorial(6)
    
def test_factorial_of_one_point_two():
    expectedResult = None
    result = exc_02_07_factorial.getFactorial(1.2)
    
    assert result == expectedResult

def test_factorial_of_number_type_is_None():
    expectedResult = None
    result = exc_02_07_factorial.getFactorial('5')
    
    assert result == expectedResult

def test_factorial_of_negative_number():
    expectedResult = None
    result = exc_02_07_factorial.getFactorial(-5)
    
    assert result == expectedResult
    
def test_factorial_of_string():
    expectedResult = None
    result = exc_02_07_factorial.getFactorial('spam spam spam spam')
    
    assert result == expectedResult


