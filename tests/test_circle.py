import numpy as np


from input.shape_circle import Circle


def test_point_inside():
  radius = 1.0
  center_coords= np.array([0.0,0.0])
  circle = Circle(radius, center_coords)
  # center is inside
  assert circle.is_point_inside(center_coords)==True
  point = np.array([0.0, radius-1.0e-7])
  assert circle.is_point_inside(point)==True
  point = np.array([0.0, radius-1.0e-15])
  assert circle.is_point_inside(point)==True # Floating arithmetic limit 
  point = np.array([0.0, radius+1.0e-7])
  assert circle.is_point_inside(point)==False 
  point = np.array([0.0, radius+1.0e-15])
  assert circle.is_point_inside(point)==False # Floating arithmetic limit 
# 
def test_point_on_perimeter():
  radius = 1.0
  center_coords= np.array([0.0,0.0])
  circle = Circle(radius, center_coords)
  point = np.array([0.0,radius])
  assert circle.is_point_inside(point)==True
  point = np.array([0.0,-radius])
  assert circle.is_point_inside(point)==True
  point = np.array([radius, 0.0])
  assert circle.is_point_inside(point)==True
  point = np.array([-radius, 0.0])
  assert circle.is_point_inside(point)==True

def test_tangent_line():
  radius = 1.0
  center_coords= np.array([0.0,0.0])
  circle = Circle(radius, center_coords)
  point_1 = np.array([-2.0, 1.0])
  point_2 = np.array([2.0, 1.0])
  assert circle.is_intersected_by_line(point_1, point_2)==True
  point_2 = np.array([2.0, 2.0])
  assert circle.is_intersected_by_line(point_1, point_2)==False

def test_line_intersection():
  radius = 1.0
  center_coords= np.array([0.0,0.0])
  circle = Circle(radius, center_coords)
  point_1 = np.array([-2.0, 1.0])
  point_2 = np.array([2.0, -1.0])
  assert circle.is_intersected_by_line(point_1, point_2)==True
  point_2 = np.array([2.0, 2.0])
  assert circle.is_intersected_by_line(point_1, point_2)==False
  point_2 = np.array([0.0, 0.0])
  assert circle.is_intersected_by_line(point_1, point_2)==True