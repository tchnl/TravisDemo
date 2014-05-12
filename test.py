# Tests.py

def test_een():
	# Test of één plus één twee is
	assert 1 + 1 == 2
	
def test_twee():
	# Test of één plus twee vijf is
	assert 1 + 2 == 5
	
def test_drie():
	# Test of je door 0 kan delen
	print 3/0
	
def test_vier():
	# Meerdere checks bij elkaar
	assert 1 + 1 == 2
	assert 2 + 2 == 4
