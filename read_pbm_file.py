"""
This is the class file for processing the image file

Author(s) : Vivek Kumar
Last Updated: December 2019
"""
import numpy as np
import cv2
import click
import matplotlib as mpl
import matplotlib.pyplot as plt


class FreeForm2d:
	"""A class to read a bitmap file and create a coordinate list"""
	def __init__(self, bitmap_file):
		self.file = bitmap_file

	def get_pixel_values(self):
		self.img = cv2.imread(self.file, cv2.IMREAD_GRAYSCALE)
		self.n_rows = self.img.shape[0]
		self.n_columns = self.img.shape[1]
		self.hx = 1./(self.n_columns-1)
		self.hy = 1./(self.n_rows-1)

	def count_non_white_pixels(self):
		self.get_pixel_values()
		counter = 0
		for i in range(self.n_rows):
			for j in range(self.n_columns):
				x_coord = j*self.hx
				y_coord = i*self.hy
				if self.img[i,j]==0:
					counter += 1
		self.non_white_pixel_count = counter

	def obtain_coordinates(self):
		self.count_non_white_pixels()
		self.vertex_array = np.zeros((self.non_white_pixel_count, 2))
		counter = 0
		for i in range(self.n_rows):
			for j in range(self.n_columns):
				x_coord = j*self.hx
				y_coord = i*self.hy
				if self.img[i,j]==0:
					self.vertex_array[counter][0] = x_coord
					self.vertex_array[counter][1] = 1-y_coord
					counter += 1

	def plot_shape(self):
		plt.scatter(self.vertex_array[:,0], self.vertex_array[:,1], marker='*')
		plt.show()


@click.command()
@click.argument('bitmap_file', type=click.Path(exists=True, dir_okay=False))
def main(bitmap_file):
	"Reading a bitmap file as shape"
	shape = FreeForm2d(bitmap_file)
	shape.obtain_coordinates()
	shape.plot_shape()
	return 0

if __name__=='__main__':
	main()



