# 
import numpy as np
import sys

from shape_circle import Circle
from shape_rectangle import Rectangle
from parse_data_class import ParseDataJSON

class Domain(Circle, Rectangle):
  """docstring for Domain"""
  def __init__(self, domain_information, origin_goal_info):
    self.domain_info = domain_information
    self.origin = np.asarray(origin_goal_info["origin"])
    self.goal = np.asarray(origin_goal_info["goal"])

  # Create the domain
  def create_domain(self):
    """ Create a domain object """
    if(self.domain_info["shape"]=="rectangle"):
      vertices = np.asarray(self.domain_info["vertices"])
      self.domain = Rectangle(vertices)
    elif(self.domain_info["shape"]=="circle"):
      radius = self.domain_info["radius"]
      center = np.asarray(self.domain_info["center"])
      self.domain = Circle(radius, center)
    else:
      print("Not Implemented")

    # Assert that origin and goal are inside the domain
    assert(self.domain.is_point_inside(self.origin)==True)
    assert(self.domain.is_point_inside(self.goal)==True)

  # Perform some sanity checks
  def is_obstacle_inside(self, obstacle):
    pass

  # Sample random point
  def

def main():
  parsed_data = ParseDataJSON("./tests/test_rrt_inputs.json")
  parsed_data.parse_data()

  domain_info = parsed_data.data_dict["Domain_Rectangle"]
  origin_goal_information = parsed_data.data_dict["Origin_Goal"]

  rrt_domain = Domain(domain_info, origin_goal_information)
  rrt_domain.create_domain()
  return 0

if __name__ == '__main__':
  main()