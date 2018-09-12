import pytest
from calc import soma

def test_soma():
	assert soma(5, 2) == 7
	assert soma(1,"4") == 5
  	assert soma("x", "z") == None
  	assert soma(1, "a") == None
	assert soma("1", "2") == 3
	assert soma(-5, -5) == -10
	assert soma(-1, 2) == 1
	assert soma("y", 2) == None
	
  
