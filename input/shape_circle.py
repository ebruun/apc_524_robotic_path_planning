# shape_circle.py
# Author(s): Vivek Kumar
import numpy as np
import math
import random

class Circle(object):
  """docstring for Circle"""
  def __init__(self, radius: float, center: np.ndarray):
    self.radius = radius
    self.center = center
  
  def is_point_inside(self, point: np.ndarray)->bool:
    if(np.linalg.norm(self.center-point) <= self.radius):
      return True
    else:
      return False

  def is_intersected_by_line(self, point_1: np.ndarray , point_2: np.ndarray)->bool:
    if(self.is_point_inside(point_1) or self.is_point_inside(point_2)):
      return True
    distance_line_to_center = abs((point_2[1]-point_1[1])*self.center[0]-(point_2[1]-point_1[1])*self.center[1]+point_2[0]*point_1[1]-point_2[1]*point_1[0])/(np.linalg.norm(point_2-point_1))
    if(distance_line_to_center <= self.radius):
      return True
    else:
      return False

  def sample_random_point(self)->np.ndarray:
    r = self.radius*math.sqrt(random.random())
    theta = random.random()*2.0*math.pi
    new_random_point = np.asarray([[self.center[0]+r*math.cos(theta), self.center[1]+r*math.sin(theta)]])
    return new_random_point