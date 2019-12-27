import numpy as np

from shape_circle import Circle
from shape_rectangle import Rectangle
from parse_data_class import ParseDataJSON

class Obstacle(Circle, Rectangle):
  """docstring for Obstacle"""
  def __init__(self, obstacle_info, origin_goal_info):
    self.obstacle_info = obstacle_info
    self.origin = np.asarray(origin_goal_info["origin"])
    self.goal = np.asarray(origin_goal_info["goal"])

  # Initialize the set of objects
  def create_obstacle(self):
    if(self.obstacle_info["shape"]=="rectangle"):
      vertices = np.asarray(self.obstacle_info["vertices"])
      self.obstacle = Rectangle(vertices)
    elif(self.obstacle_info["shape"]=="circle"):
      radius = self.obstacle_info["radius"]
      center = np.asarray(self.obstacle_info["center"])
      self.obstacle = Circle(radius, center)
    else:
      print("Not Implemented")
    # Assert that origin and domain are not inside the obstacle
    assert(self.domain.is_point_inside(self.origin)==False)
    assert(self.domain.is_point_inside(self.goal)==False)


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