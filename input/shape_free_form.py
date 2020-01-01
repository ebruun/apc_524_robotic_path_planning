"""
This is the class file for processing the image file

Author(s) : Vivek Kumar
Last Updated: December 2019
"""
import numpy as np
import cv2
import click
from scipy.spatial import ConvexHull
from scipy.spatial import Delaunay
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys

class FreeForm2d:
  """A class to read a bitmap file and create a coordinate list"""
  def __init__(self, bitmap_file):
    self.file = bitmap_file
    self.img = cv2.imread(self.file, cv2.IMREAD_GRAYSCALE)
    self.n_rows = self.img.shape[0]
    self.n_columns = self.img.shape[1]
    self.hx = 1./(self.n_columns-1)
    self.hy = 1./(self.n_rows-1)

  def obtain_outline_coordinates(self):
    self.edges = cv2.Canny(self.img, 100, 200)
    number_of_edge_points = np.count_nonzero(self.edges!=0)
    self.boundary_vertex_array = [[j*self.hx, 1.0-i*self.hy] for i in range(self.n_rows) for j in range(self.n_columns) if self.edges[i,j]!=0]
    self.boundary_vertex_array = np.asarray(self.boundary_vertex_array)
    
  def obtain_coordinates(self):
    self.non_white_pixel_count = np.count_nonzero(self.img==0)
    self.all_points_array = [[j*self.hx, 1.0-i*self.hy] for i in range(self.n_rows) for j in range(self.n_columns) if self.img[i,j]==0]
    self.all_points_array = np.asarray(self.all_points_array)

  def is_point_inside(self, point):
    pass

  def is_intersected_by_line():
    pass


@click.command()
@click.argument('bitmap_file', type=click.Path(exists=True, dir_okay=False))
def main(bitmap_file):
  "Reading a bitmap file as shape"
  shape = FreeForm2d(bitmap_file)
  # shape.get_pixel_values()
  shape.obtain_outline_coordinates()
  # shape.count_non_white_pixels()
  # print(shape.non_white_pixel_count)
  # shape.obtain_coordinates()
  shape.plot_shape()
  return 0

if __name__=='__main__':
  main()



