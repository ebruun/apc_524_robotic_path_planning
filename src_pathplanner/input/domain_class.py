# domain_class.py
# Author(s): Vivek Kumar
# Last Updated: January 2019
import numpy as np
import sys
# Package modules
from input.shape_circle import Circle
from input.shape_rectangle import Rectangle
from input.shape_free_form import FreeForm2D
from input.obstacles_class import Obstacle
from input.parse_data_class import ParseDataJSON

class Domain():
  """A class used to represent the domain in the RRT software.

  Domain represents the spatial expanse in which the RRT algorithms looks for paths to reach the goal from the starting point (origin)
  """
  def __init__(self, domain_info, obstacle_info, origin_goal_info):
    """Constructor method

    Parameters:
      domain_info:
        Dictionary containing information about the domain
      obstacle_info:
        Dictionary containing information about the obstacles in the domain
      origin_goal_info:
        Dictionary containing information about the origin and goal

    Attributes:
      domain_info:
        Dictionary containing information about the domain
      dim :
        Dimensions of the domain
      domain_shape:
        The shape of the domain
      obstacle_info:
        Dictionary containing information about the obstacles in the domain
      origin_goal_info:
        Dictionary containing information about the origin and goal
      origin:
        The point from where the rrt algorithm begins
      goal_info:
        The separated goal information

    """
    self.domain_info = domain_info
    self.dim = self.domain_info["dim"]
    self.domain_shape = self.domain_info["shape_type"]
    self.obstacle_info = obstacle_info
    self.origin_goal_info = origin_goal_info

    self.origin = np.asarray(self.origin_goal_info["origin"])
    self.goal_info = self.origin_goal_info["goals"]

    self.create_domain()
    self.create_obstacles()
    self.create_goals()

  # Create the domain
  def create_domain(self):
    """Creates the domain based on the shape and geometrical information provided in the domain information list
    """
    if(self.domain_shape=="rectangle"):
      assert(self.dim==2)
      self.domain = Rectangle(self.domain_info)
    elif(self.domain_shape=="circle"):
      assert(self.dim==2)
      self.domain = Circle(self.domain_info)
    elif(self.domain_shape=="free_form"):
      assert(self.dim==2)
      self.domain = FreeForm2D(self.domain_info)
    else:
      raise Exception('The domain shape is not implemented')

    # Assert that origin and goal are inside the domain
    assert(self.domain.is_point_inside(self.origin)==True)
    # assert(self.domain.is_point_inside(self.goal)==True)


  def create_obstacles(self):
    """Creates the obstacles based on the shape and geometrical information provided in the obstacle information list
    """
    self.obstacles = [Obstacle(self.obstacle_info[key], self.origin_goal_info).obstacle for key in self.obstacle_info]
    self.is_obstacle_inside()

  def create_goals(self):
    """Creates the goals based on the shape and geometrical information provided in the origin-goal information list
    """
    self.goals = [Obstacle(self.goal_info[key], self.origin_goal_info).obstacle for key in self.goal_info]

  # Perform some sanity checks
  def is_obstacle_inside(self):
    pass