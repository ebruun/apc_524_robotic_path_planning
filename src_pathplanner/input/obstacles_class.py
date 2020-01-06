# obstacle_class.py
# Author(s): Vivek Kumar
# Last Updated: January 2019

import numpy as np

from input.shape_circle import Circle
from input.shape_rectangle import Rectangle
from input.shape_free_form import FreeForm2D
from input.parse_data_class import ParseDataJSON


class Obstacle():
  """A class used to represent the obstacles in the RRT software.

  Obstacles denote regions of the domain which are inaccessible to the robot. Hence a new point in the path cannot be generated inside the obstacles

  :param obstacle_info: The information of the obstacle being created
  :type obstacle_info: dict
  :param origin_goal_info: The coordinates of the path starting location (called origin) and where the path should end (called goal)
  :type origin_goal_info: dict
  
  """
  def __init__(self, obstacle_info, origin_goal_info):
    """Constructor method
    """
    self.obstacle_info = obstacle_info
    self.origin = np.asarray(origin_goal_info["origin"])
    self.goal = np.asarray(origin_goal_info["goal"])

    self.create_obstacle()

  def create_obstacle(self):
    """Returns the obstacle object
    """
    if(self.obstacle_info["shape"]=="rectangle"):
      vertices = np.asarray(self.obstacle_info["vertices"])
      self.obstacle = Rectangle(vertices)
    elif(self.obstacle_info["shape"]=="circle"):
      radius = self.obstacle_info["radius"]
      center = np.asarray(self.obstacle_info["center"])
      self.obstacle = Circle(radius, center)
    elif(self.obstacle_info["shape"]=="free_form"):
      self.obstacle = FreeForm2D(self.obstacle_info["bitmap_file"])
    else:
      raise Exception('The obstacle shape is not implemented')

    # Assert that origin and domain are not inside the obstacle
    assert(self.obstacle.is_point_inside(self.origin)==False)
    assert(self.obstacle.is_point_inside(self.goal)==False)

