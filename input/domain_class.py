# domain_class.py
# Author(s): Vivek Kumar
# Last Updated: January 2019
import numpy as np
import sys

from input.shape_circle import Circle
from input.shape_rectangle import Rectangle
from input.parse_data_class import ParseDataJSON

class Domain():
  """A class used to represent the domain in the RRT software.

  Domain represents the spatial expanse in which the RRT algorithms looks for paths to reach the goal from the starting point (origin)

  :param domain_information: The information of the domain being created
  :type domain_information: dict
  :param origin_goal_info: The coordinates of the path starting location (origin) and where the path should end (goal)
  :type origin_goal_info: dict
  
  """
  def __init__(self, domain_information, origin_goal_info):
    """Constructor method
    """
    self.domain_info = domain_information
    self.origin = np.asarray(origin_goal_info["origin"])
    self.goal = np.asarray(origin_goal_info["goal"])

    self.create_domain()
  # Create the domain
  def create_domain(self):
    """Creates the domain based on the shape and geometrical information provided in the domain information list
    """
    if(self.domain_info["shape"]=="rectangle"):
      vertices = np.asarray(self.domain_info["vertices"])
      self.domain = Rectangle(vertices)
    elif(self.domain_info["shape"]=="circle"):
      radius = self.domain_info["radius"]
      center = np.asarray(self.domain_info["center"])
      self.domain = Circle(radius, center)
    else:
      raise Exception('The obstacle shape is not implemented')

    # Assert that origin and goal are inside the domain
    assert(self.domain.is_point_inside(self.origin)==True)
    assert(self.domain.is_point_inside(self.goal)==True)

  # Perform some sanity checks
  def is_obstacle_inside(self, obstacle):
    pass