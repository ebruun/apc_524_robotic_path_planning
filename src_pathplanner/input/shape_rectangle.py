# shape_rectangle.py
# Author(s): Vivek Kumar
# Last Updated: January 2019
import numpy as np

from input.shape import Shape

class Rectangle(Shape):
  """A class used to create rectangular objects which could act as domain or obstacle shape

  :param shape_info: information about the lower left and upper right corners
  :type shape_info: dict
  
  """
  def __init__(self, shape_info:dict):
    """Constructor method
    
    This is the constructor of the the rectangle class. A rectangle object is initialized by specifying the lower left corner and upper right corner points.

    """
    super().__init__(shape_info)

    self.ll_corner = np.asarray(shape_info['lower_left'])
    self.ur_corner = np.asarray(shape_info['upper_right'])
    # Assert the order of points
    assert(self.ll_corner[0] < self.ur_corner[0])
    assert(self.ll_corner[1] < self.ur_corner[1])

    # Compute the vertices
    self.vertices = np.array([[self.ll_corner[0], self.ll_corner[1]], [self.ur_corner[0],self.ll_corner[1]], [self.ur_corner[0], self.ur_corner[1]], [self.ll_corner[0], self.ur_corner[1]]])
    
    # The dimensions of the rectangle
    self.width = abs(self.vertices[0][0]-self.vertices[2][0])
    self.height = abs(self.vertices[0][1]-self.vertices[2][1])
    # The centroid of the rectangle
    self.centroid = np.mean(self.vertices, axis=0)


  def is_point_inside(self, point: np.ndarray)->bool:
    """Checks if a given point is inside the circle

    Find the method here: https://math.stackexchange.com/questions/190111/how-to-check-if-a-point-is-inside-a-rectangle

    Currently the implementation is complicated as it takes into account that the rectangle could be a rotated one and not axis-aligned.
    
    Returns:
      bool.::

        True -- Point is inside
        False -- Point is not inside

    """
    if ((0.0 <= (np.dot(self.vertices[0]-point, self.vertices[0]-self.vertices[1])) <= (np.dot(self.vertices[0]-self.vertices[1], self.vertices[0]-self.vertices[1]))) and ( 0 <= (np.dot(self.vertices[0]-point, self.vertices[0]-self.vertices[3])) <= (np.dot(self.vertices[0]-self.vertices[3], self.vertices[0]-self.vertices[3])))):
      return True
    else:
      return False

  # Possibly move to a line class
  def check_line_intersection(self, point_1:np.ndarray, point_2:np.ndarray, point_3:np.ndarray, point_4:np.ndarray)->bool:
    """Checks if two line segments defined by the end points (point_1, point_2) and (point_3, point_4) intersect each other

    Find the method here:

    https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
    
    Returns:
      bool.::

        True -- The two line segments intersect
        False -- The two line segments do not intersect

    """
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

  def is_intersected_by_edge(self, point_1:np.ndarray, point_2: np.ndarray)->bool:
    """Checks if the line segment connecting two points intersects the rectangle
    
    Here the intersection of the line segment defined by the points (point_1 and point_2) is tested against all the sides of the rectangle. Since it is assumed that the points are always outside the rectangle if the edge intersects any side it is bound to cross the rectangle

    Returns:
      bool::

        True -- The line intersects or is tangent
        False -- The does not intersect
        
    """
    assert(self.is_point_inside(point_1)==False)
    assert(self.is_point_inside(point_2)==False)
    # The algorithm below assumes that the two points being connected are outside the rectangle
    # TO DO: Make it a loop so that can be extended to n-sided polygon
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
    """Generates a random point in the rectangle

    Returns:
      A new point::
        
    """
    new_random_point = np.random.rand(2)
    new_random_point[0] = new_random_point[0]*(self.width)+self.vertices[0][0]
    new_random_point[1] = new_random_point[1]*(self.height)+self.vertices[0][1]
    return new_random_point