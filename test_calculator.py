from calculator import add, subtract, multiply, divide

def test_add():
	assert add(2,3) == 5

def test_divide():
	assert divide(6,2) == 3

def test_subtract():
	assert subtract(8,4) == 4

def test_multiply():
	assert multiply(3,2) == 6

def test_zero_multiply():
	# Arrange
	a, b = 12, 0
	# Act
	result =  multiply(a, b)
	# Assert
	assert result == 0

