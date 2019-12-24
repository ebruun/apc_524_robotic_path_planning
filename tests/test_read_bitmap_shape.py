"""
This is the test file for the class to read the FreeForm class

Author(s) : Vivek Kumar
Last Updated: December 2019
"""
import numpy as np
import cv2
import click
import matplotlib as mpl
import matplotlib.pyplot as plt
from pytest import approx

from read_pbm_file import FreeForm2d

def test_get_pixel_values():
	shape = FreeForm2d('./tests/test_rectangle.pbm')
	shape.get_pixel_values()
	assert shape.n_rows == 63
	assert shape.n_columns == 200
	assert shape.hx == 1./199.
	assert shape.hy == 1./62.

def test_count_non_white_pixels():
	shape = FreeForm2d('./tests/test_rectangle.pbm')
	shape.count_non_white_pixels()
	assert shape.non_white_pixel_count == 1848

def test_obtain_coordinates():
	shape = FreeForm2d('./tests/test_rectangle.pbm')
	shape.obtain_coordinates()
	# Left top corner
	assert shape.vertex_array[0][0] == approx(0.020100503)
	assert shape.vertex_array[0][1] == approx(0.870967742)

def test_is_point_inside():
	shape = FreeForm2d('./tests/test_rectangle.pbm')
	point = np.array()

