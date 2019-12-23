# shape_circle.py
# Author(s): Vivek Kumar
import numpy as np

# Special case of polygon class
class Rectangle():
  """docstring for Rectangle"""
  def __init__(self, vertices: np.ndarray):
    self.vertices = vertices
    # Add an assert that the user does not input random order of points

  def is_point_inside(self, point: np.ndarray)->bool:
    # Add documentation or links
    if ((0.0 <= (np.dot(self.vertices[0]-point, self.vertices[0]-self.vertices[1])) <= (np.dot(self.vertices[0]-self.vertices[1], self.vertices[0]-self.vertices[1]))) and ( 0 <= (np.dot(self.vertices[0]-point, self.vertices[0]-self.vertices[3])) <= (np.dot(self.vertices[0]-self.vertices[3], self.vertices[0]-self.vertices[3])))):
      return True
    else:
      return False

  def check_two_line_segment_intersection(line_1: np.ndarray, line_2:np.ndarray)->bool:
    if()
    return False


  def is_intersected_by_line(self, point_1:np.ndarray, point_2: np.ndarray)->bool:
    if(self.is_point_inside(point_1) or self.is_point_inside(point_2)):
      return True

    pass
