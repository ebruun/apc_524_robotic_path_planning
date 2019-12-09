"""
This is the test file for the free form

Author(s) : Vivek Kumar
Last Updated: December 2019
"""
import numpy as np
import cv2
import click
import matplotlib as mpl
import matplotlib.pyplot as plt

from read_pbm_file import FreeForm2d

def test_get_pixel_values():
	shape = FreeForm2d('./tests/circle.pbm')
	shape.get_pixel_values()
	assert shape.n_rows == 200
	assert shape.n_columns == 200
	assert shape.hx == 1./199.
	assert shape.hy == 1./199.





