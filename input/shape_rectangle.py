# shape_circle.py
# Author(s): Vivek Kumar
import numpy as np

# Special case of polygon class
class Rectangle():
  """docstring for Rectangle"""
  def __init__(self, vertices: np.ndarray):
    self.vertices = vertices
    self.width = abs(vertices[0][0]-vertices[2][0])
    self.height = abs(vertices[0][1]-vertices[2][1])
    # Add an assert that the user does not input random order of points

  def is_point_inside(self, point: np.ndarray)->bool:
    # Add documentation or links
    if ((0.0 <= (np.dot(self.vertices[0]-point, self.vertices[0]-self.vertices[1])) <= (np.dot(self.vertices[0]-self.vertices[1], self.vertices[0]-self.vertices[1]))) and ( 0 <= (np.dot(self.vertices[0]-point, self.vertices[0]-self.vertices[3])) <= (np.dot(self.vertices[0]-self.vertices[3], self.vertices[0]-self.vertices[3])))):
      return True
    else:
      return False

  # Possibly move to a line class
  # Check if 2 lines described by points (p1,p2) and (p3,p4) intersects
  def check_line_intersection(self, point_1:np.ndarray, point_2:np.ndarray, point_3:np.ndarray, point_4:np.ndarray)->bool:

    denominator = (point_1[0]-point_2[0])*(point_3[1]-point_4[1])- (point_1[1]-point_2[1])*(point_3[0]-point_4[0])
    if(denominator == 0):
      # If 0, then the lines are parallel
      return False
    else:
      numerator_alpha = (point_1[0]-point_3[0])*(point_3[1]-point_4[1]) -(point_1[1]-point_3[1])*(point_3[0]-point_4[0])
      if (0.0 <= (numerator_alpha/denominator) <= 1.0):
        numerator_beta = -1.*((point_1[0]-point_2[0])*(point_1[1]-point_3[1])-(point_1[1]-point_2[1])*(point_1[0]-point_3[0]))
        if(0.0 <= (numerator_beta/denominator) <= 1.0):
          return True
        else:
          return False
      else:
        return False

  def is_intersected_by_line(self, point_1:np.ndarray, point_2: np.ndarray)->bool:
    assert(self.is_point_inside(point_1)==False)
    assert(self.is_point_inside(point_2)==False)
    # The algorithm below assumes that the two points being connected are outside the rectangle
    # Side 1
    if(self.check_line_intersection(self.vertices[0], self.vertices[1], point_1, point_2)):
      return True

    if(self.check_line_intersection(self.vertices[1], self.vertices[2], point_1, point_2)):
      return True
    if(self.check_line_intersection(self.vertices[2], self.vertices[3], point_1, point_2)):
      return True
    if(self.check_line_intersection(self.vertices[3], self.vertices[0], point_1, point_2)):
      return True
    return False

  def sample_random_point(self)->np.ndarray:
    new_random_point = np.random.rand(2)
    new_random_point[0] = new_random_point[0]*(self.width)+self.vertices[0][0]
    new_random_point[1] = new_random_point[1]*(self.height)+self.vertices[0][1]
    print(new_random_point)
    return new_random_point


def main():
  p1 = np.array([-2,0])
  p2 = np.array([2,0.5])
  p3 = np.array([1,-1])
  p4 = np.array([1,1])

  print(check_line_intersection(p1,p2,p3,p4))

  return 0
if __name__ == '__main__':
  main()