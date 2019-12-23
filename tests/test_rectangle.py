import numpy as np


from input.shape_rectangle import Rectangle


def test_point_inside():
  vertices = np.array([[-1.0, -1.0],[1.0,-1.0],[1.0,1.0],[-1.0,1.0]])

  rectangle = Rectangle(vertices)
  point = np.array([0.0,0.0])
  assert(rectangle.is_point_inside(point)==True)
  point = np.array([10.0,0.0])
  assert(rectangle.is_point_inside(point)==False)
  # Test edge cases
  # Tests for points very close to the vertices
  point = np.array([1.0,1.0+1.0e-15])
  assert(rectangle.is_point_inside(point)==False)
  point = np.array([1.0,1.0-1.0e-15])
  assert(rectangle.is_point_inside(point)==True)

  point = np.array([1.0-1.0e-15,-1.0+1.0e-15])
  assert(rectangle.is_point_inside(point)==True)
  point = np.array([1.0+1.0e-15,-1.0-1.0e-15])
  assert(rectangle.is_point_inside(point)==False)
  # Tests for points very close to the edges
