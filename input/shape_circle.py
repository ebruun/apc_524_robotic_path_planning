# shape_circle.py
# Author(s): Vivek Kumar
import numpy as np
# from shape import Shape

class Circle():
  """docstring for Circle"""
  def __init__(self, radius: float, center: np.ndarray):
    self.radius = radius
    self.center = center
  
  def is_point_inside(self, pt: np.ndarray)->bool:
    if(np.linalg.norm(self.center-pt) <= self.radius):
      return True
    else:
      return False

  def is_intersected_by_line(self, pt1: np.ndarray , pt2: np.ndarray):
    if(self.is_point_inside(pt1) or self.is_point_inside(pt2)):
      return True
    distance_line_to_center = abs((pt2[1]-pt1[1])*self.center[0]-(pt2[1]-pt1[1])*self.center[1]+pt2[0]*pt1[1]-pt2[1]*pt1[0])/(np.linalg.norm(pt2-pt1))
    if(distance_line_to_center <= self.radius):
      return True
    else:
      return False