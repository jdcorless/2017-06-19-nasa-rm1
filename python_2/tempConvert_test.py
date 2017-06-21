# this file begins or ends with test_ or _test
import tempConvert

def test_temps():
	assert(tempConvert.f_to_k(32) == 273.15)

def test_temp_again():
	assert(tempConvert.f_to_k(212) == 373.15)
