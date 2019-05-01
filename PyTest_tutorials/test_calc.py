#import calc as sut
import pytest
from pytest import fixture


@fixture
def sut():
	import calc
	return calc

#Basic Examples
def test_multiply(sut, ):
	# Setup
	num1 = 2
	num2 = 3
	expected_result = 6
	# Exercise
	result = sut.multiply(num1, num2)
	# Verify
	assert result == expected_result

def test_divide(sut):
	# Setup
	num1 = 10
	num2 = 5
	expected_result = 2
	# Exercise
	result = sut.divide(num1, num2)
	# Verify
	assert result == expected_result


#Parametrized Examples
@pytest.mark.parametrize("num1, num2, expected_result", [(10,2,20), (2,2,4), (7,2,14)])
def test_multiply_params(sut, num1, num2, expected_result):
	# Exercise
	result = sut.multiply(num1, num2)
	# Verify
	assert result == expected_result

@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*7", 42),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
