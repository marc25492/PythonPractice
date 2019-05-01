import pytest


# Basic Example
def test_file1_method1():
	x=5
	y=6
	assert x+1 == y,"test failed"
	#assert x == y,"test failed"

def test_file1_method2():
	x=5
	y=6
	assert x+1 == y,"test failed"


# Test a Fixture
@pytest.fixture
def supply_a_b_c():
	a=1
	b =2
	c=3
	return [a,b,c]

def test_addition(supply_a_b_c):
    assert supply_a_b_c[0] + supply_a_b_c[1] == supply_a_b_c[2]


# Test a Method
def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'
    assert capital_case('semaphore') != 'semaphore'
