# shape_rectangle.py
# Author(s): Vivek Kumar
# Last Updated: January 2019

import numpy as np
from scipy.spatial import ConvexHull
from scipy.spatial import Delaunay
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
import math
import random

import cv2

from input.shape import Shape

class FreeForm2D(Shape):
  """A class used to create free form shape as a domain or obstacleshape

  :param shape_info: information about the bitmap file
  :type shape_info: dict
  
  """
  def __init__(self, shape_info:dict):

    super().__init__(shape_info)

    self.file = shape_info['bitmap_file']
    self.bb_lower_left = shape_info['bb_lower_left'] # The lower left location of the bounding box
    self.bb_upper_right = shape_info['bb_upper_right'] # The upper right location of the bounding box
    self.obtain_geometric_info()


  def obtain_geometric_info(self):
    """Computes geomterical information from the bitmap points

    This function converts the bitmap 0,1 array to coordinates and computes geometrical properties such as centroid and bounding box for the free form shape
    """
    self.img = cv2.imread(self.file, cv2.IMREAD_GRAYSCALE)

    self.n_rows = self.img.shape[0]
    self.n_columns = self.img.shape[1]
    self.hx = 1./(self.n_rows-1) # This makes sure that the x-values are b/w 0-1
    self.hy = (1./(self.n_columns-1)) *((self.n_rows-1)/(self.n_columns-1))
    
    self.all_points_array = [[j*self.hx, 1.0-i*self.hy] for i in range(self.n_rows) for j in range(self.n_columns) if self.img[i,j]==0]
    self.all_points_array = np.asarray(self.all_points_array)

    # The left most corner 
    self.x_min_val = np.min(self.all_points_array[:,0])
    self.y_min_val = np.min(self.all_points_array[:,1])
    

    # Traslate the coordinates
    self.all_points_array[:,0] = self.all_points_array[:,0]-self.x_min_val
    self.all_points_array[:,1] = self.all_points_array[:,1]-self.y_min_val
    
    # The original bounding box
    self.x_min_val = np.min(self.all_points_array[:,0])
    self.y_min_val = np.min(self.all_points_array[:,1])
    self.x_max_val = np.max(self.all_points_array[:,0])
    self.y_max_val = np.max(self.all_points_array[:,1])
    
    original_bb_width = self.x_max_val - self.x_min_val
    original_bb_height = self.y_max_val - self.y_min_val

    new_bb_width = self.bb_upper_right[0] - self.bb_lower_left[0]
    new_bb_height = self.bb_upper_right[1] - self.bb_lower_left[1]

    x_scale = new_bb_width/original_bb_width
    y_scale = new_bb_height/original_bb_height

    self.all_points_array[:,0] = self.all_points_array[:,0]*x_scale
    self.all_points_array[:,1] = self.all_points_array[:,1]*y_scale

    self.all_points_array[:,0] = self.all_points_array[:,0]+self.bb_lower_left[0]
    self.all_points_array[:,1] = self.all_points_array[:,1]+self.bb_lower_left[1]

    self.x_min_val = np.min(self.all_points_array[:,0])
    self.y_min_val = np.min(self.all_points_array[:,1])
    self.x_max_val = np.max(self.all_points_array[:,0])
    self.y_max_val = np.max(self.all_points_array[:,1])

    self.hx = self.hx*x_scale
    self.hy = self.hy*y_scale
    # Compute the centroid of the shape
    self.centroid = np.mean(self.all_points_array, axis=0)

  # Check if a new point is inside the shape
  # This is slow!!!
  def is_point_inside(self, point:np.ndarray)->bool:
    """Checks if a given point is inside the circle

    Computes the distance of the point from the center of the circle and compares it with the radius
    
    Returns:
      bool.::

        True -- Point is inside
        False -- Point is not inside

    """
    # If inside_bounding box
    if(point[0] < self.x_min_val or point[0] > self.x_max_val or point[1] < self.y_min_val or point[1] > self.y_max_val):
      return False
    else:
      # Select all the points whose y values are within a tolerance of max(2.*hx, 2.*hy)
      shape_points = self.all_points_array[self.all_points_array[:,1] < point[1]+2.1*self.hy]
      shape_points = shape_points[shape_points[:,1] > point[1] -2.1*self.hy]
      number_of_shape_points = shape_points.shape[0]
      _eps = 1.0e-1
      test_radius = max(self.hx,self.hy)*(2.+_eps)
      for shape_point in shape_points:
        if(np.linalg.norm(point-shape_point) <= test_radius):
          return True
      return False

  def is_intersected_by_edge(self, point_1:np.ndarray, point_2: np.ndarray)->bool:
    """Checks if the line segment connecting two points intersects the free
    
    The method is adopted from `here`_. It is assumed that both the points are outside the circle

    .. _here: https://math.stackexchange.com/questions/275529/check-if-line-intersects-with-circles-perimeter

    Returns:
      bool::

        True -- The line intersects or is tangent
        False -- The does not intersect
        
    """
    assert self.is_point_inside(point_1)==False
    assert self.is_point_inside(point_2)==False
    
    # Compute the number of points based on the hx value
    length_of_edge = np.linalg.norm(point_1-point_2)
    # Divide the edge into appropriate number of segments
    n_divisions = math.ceil(length_of_edge*(1./self.hx))
    if point_1[0] == point_2[0]:
      points_to_test = [[point_1[0], point_1[1]+(i+1)*((point_2[1]-point_1[1])/n_divisions)] for i in range(n_divisions-1)]
    else:
      line_slope = (point_2[1]-point_1[1])/(point_2[0]-point_1[0])
      points_to_test = [[point_1[0]+(i+1)*(point_2[0]-point_1[0])/(n_divisions), line_slope*(point_1[0]+(i+1)*(point_2[0]-point_1[0])/(n_divisions) - point_1[0])+ point_1[1]] for i in range(n_divisions-1)]

    for point in points_to_test:
      if(self.is_point_inside(point)):
        return True
    return False

  def sample_random_point(self)->np.ndarray:
    """Generates a random point in the shape free form

    Returns:
      A new point

    """
    random_point = (self.all_points_array[np.random.randint(self.all_points_array.shape[0], size=1), :]).flatten()
    delta = np.random.rand(2)

    delta[0] = delta[0]*self.hx
    delta[1] = delta[1]*self.hy
    random_point = random_point+delta
    while(not self.is_point_inside(random_point)):
      random_point = (self.all_points_array[np.random.randint(self.all_points_array.shape[0], size=1), :]).flatten() + delta
    return random_point

