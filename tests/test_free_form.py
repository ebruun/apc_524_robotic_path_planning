"""
This is the test file for the class to read the FreeForm class

Author(s) : Vivek Kumar
Last Updated: December 2019
"""
from pytest import approx
import numpy as np
from input.shape_free_form import FreeForm2D


def test_get_pixel_values():
  shape_info = {'bitmap_file': './tests/test_rectangle.pbm'}
  free_shape = FreeForm2D(shape_info)
  assert free_shape.n_rows == 55
  assert free_shape.n_columns == 200
  assert free_shape.hx == 1./54.
  assert free_shape.hy == (1./199.)*(54./199.)

def test_is_point_inside():
  shape_info = {'bitmap_file': './tests/test_rectangle.pbm'}
  free_shape = FreeForm2D(shape_info)
  point_1 = np.array([1.8,0.03])
  assert(free_shape.is_point_inside(point_1)==True)
  point_2 = np.array([3.4,0.063])
  assert(free_shape.is_point_inside(point_2)==False)
  assert(free_shape.is_point_inside(free_shape.centroid)==True)

def test_is_intersected_by_edge():
  shape_info = {'bitmap_file': './tests/test_rectangle.pbm'}
  free_shape = FreeForm2D(shape_info)
  point_1 = np.array([-1.0, 0.0])
  point_2 = np.array([4.0, 0.3])
  assert(free_shape.is_intersected_by_edge(point_1, point_2)==True)

  point_3 = np.array([-0.062, 0.0])
  point_4 = np.array([3.6, 0.062])
  assert(free_shape.is_intersected_by_edge(point_3, point_4)==True)

  point_5 = np.array([1.0, 10.0])
  point_6 = np.array([1.0, 0.1])
  assert(free_shape.is_intersected_by_edge(point_5, point_6)==False)


def test_new_random_point():
  shape_info = {'bitmap_file': './tests/test_rectangle.pbm'}
  free_shape = FreeForm2D(shape_info)
  for i in range(10):
    new_random_point = free_shape.sample_random_point()
    assert(free_shape.is_point_inside(new_random_point)==True)