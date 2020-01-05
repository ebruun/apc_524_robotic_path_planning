"""
This is the test file for the class to read the FreeForm class

Author(s) : Vivek Kumar
Last Updated: December 2019
"""
from pytest import approx
from matplotlib.pyplot import *
sys.path.append(".")

from input.shape_free_form import FreeForm2D

def test_get_pixel_values():
  shape = FreeForm2D('./tests/test_rectangle.pbm')
  assert shape.n_rows == 55
  assert shape.n_columns == 200
  assert shape.hx == 1./54.
  assert shape.hy == (1./199.)*(54./199.)

def test_count_non_white_pixels():
  shape = FreeForm2D('./tests/test_rectangle.pbm')
  assert shape.non_white_pixel_count == 9024

def test_obtain_coordinates():
  shape = FreeForm2D('./tests/test_rectangle.pbm')
  # Left top corner
  pass

def test_create_outer_boundary():
  print("all good")
  shape = FreeForm2D('./tests/test_rectangle.pbm')
  pass

def test_is_point_inside():
  shape = FreeForm2D('./tests/test_rectangle.pbm')
  pass