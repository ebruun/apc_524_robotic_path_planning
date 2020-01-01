"""
This is the test file for the class to read the FreeForm class

Author(s) : Vivek Kumar
Last Updated: December 2019
"""
from pytest import approx

from input.shape_free_form import FreeForm2d

def test_get_pixel_values():
	shape = FreeForm2d('./tests/test_rectangle.pbm')
	assert shape.n_rows == 55
	assert shape.n_columns == 200
	assert shape.hx == 1./199.
	assert shape.hy == 1./54.

def test_count_non_white_pixels():
	shape = FreeForm2d('./tests/test_rectangle.pbm')
	shape.obtain_coordinates()
	assert shape.non_white_pixel_count == 9024

def test_obtain_coordinates():
	shape = FreeForm2d('./tests/test_rectangle.pbm')
	shape.obtain_coordinates()
	# Left top corner
	assert shape.all_points_array[0][0] == approx(0.020100503)

def test_is_point_inside():
	shape = FreeForm2d('./tests/test_rectangle.pbm')
	pass

