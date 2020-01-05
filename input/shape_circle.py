# shape_circle.py
# Author(s): Vivek Kumar
# Last Updated: January 2019
import numpy as np
import math
import random

class Circle():
  """A class used to create circular objects which could act as domain or obstacle shape
  
  :param shape_info: Radius and center information
  :type shape_info: dict
  
  """
  def __init__(self, shape_info:dict):
    """Constructor method
    """
    self.radius = shape_info["radius"]
    self.center = shape_info["center"]
  
  def is_point_inside(self, point: np.ndarray)->bool:
    """Checks if a given point is inside the circle

    Computes the distance of the point from the center of the circle and compares it with the radius
    
    Returns:
      bool.::

        True -- Point is inside
        False -- Point is not inside

    """
    if(np.linalg.norm(self.center-point) <= self.radius):
      return True
    else:
      return False

  def is_intersected_by_edge(self, point_1: np.ndarray , point_2: np.ndarray)->bool:
    """Checks if the line segment connecting two points intersects the circle
    
    The method is adopted from `here`_. It is assumed that both the points are outside the circle

    .. _here: https://math.stackexchange.com/questions/275529/check-if-line-intersects-with-circles-perimeter

    Returns:
      bool::

        True -- The line intersects or is tangent
        False -- The does not intersect
        
    """
    assert(self.is_point_inside(point_1)==False)
    assert(self.is_point_inside(point_2)==False)

    # Move the coordinate system so that the center is at (0,0)
    point_1[0] = point_1[0] - self.center[0]
    point_1[1] = point_1[1] - self.center[1]

    point_2[0] = point_2[0] - self.center[0]
    point_2[1] = point_2[1] - self.center[1]

    # Check the link for the details of the implementation
    a = (point_2[0]-point_1[0])**2 + (point_2[1]-point_1[1])**2

    b = 2.0*(point_1[0]*(point_2[0]-point_1[0])+point_1[1]*(point_2[1]-point_1[1]))

    c = point_1[0]**2 + point_1[1]**2 - self.radius**2

    print(b**2 - 4.0*a*c)
    if(b**2 - 4.0*a*c < 0):
      return False

    if(b**2 -4.*a*c ==0):
      if(0 <= -b/(2.0*a) <= 1):
        return True

    t_1 = (-b + math.sqrt(b**2 -4.*a*c))/(2.0*a)
    t_2 = (-b - math.sqrt(b**2 -4.*a*c))/(2.0*a)
    print(t_1, t_2)
    if((0 <= t_1 <=1) and (0 <= t_2 <=1)):
      return True

    return False

  def sample_random_point(self)->np.ndarray:
    """Generates a random point in the circle

    Returns:
      A new point::
        
    """
    r = self.radius*math.sqrt(random.random())
    theta = random.random()*2.0*math.pi
    new_random_point = np.asarray([[self.center[0]+r*math.cos(theta), self.center[1]+r*math.sin(theta)]])
    return new_random_point