# rrt_star.py
# Author(s): Edvard Bruun

import numpy as np

from algorithm.rrt import RRT
from input.shape_circle import Circle

#Delete later
from output.plot1 import Plot
import matplotlib.pyplot as plt

class RRT_Star(RRT):
	""" A class for RRT algorithm.

	"""

	def __init__(self,domain,recorder,params):
		super().__init__(domain,recorder,params)
		self.neighbor_offset = 1.1 #10% larger radius to look in
		self.neighbor_indices = []
		self.neighbor_dist = []

		self.toggle = 0 #Plot things


	def rrt_step(self,trial):
		print("\nVertex", trial+1)
		
		self.new_q = self.new_config()
		self.new_v, self.new_parent, self.new_cost = self.new_vertex()

		while self.is_new_edge_blocked(self.recorder.vertices[self.new_parent],self.new_v):	
			self.new_q = self.new_config()
			self.new_v, self.new_parent, self.new_cost = self.new_vertex()				
		
		self.recorder.vertices[trial,:] = self.new_v

		self.plot_tests(trial,trial+1, self.toggle)

		# New code for RRT_Star
		print("Neighborhood calcs")
		self.find_vertices_in_neighborhood()
		self.new_parent,self.new_cost = self.find_parent_shortest_path()

		self.recorder.parents[trial] = self.new_parent 
		self.recorder.costs[trial] = self.update_path_cost(self.new_parent,self.new_cost)

		self.plot_tests(trial+1,trial+1,self.toggle)

		print("\nREWIRE")
		self.rewire(trial)

		self.plot_tests(trial+1,trial+1,self.toggle)


	def find_vertices_in_neighborhood(self):
		"""fill out
		"""
		del self.neighbor_indices[:]
		del self.neighbor_dist[:]

		offset = self.neighbor_offset
		neighbor_circle = Circle({'radius':offset*self.params["neighborhood"], 'center':self.new_v})
		
		indices_in_box = self.find_indices_in_extents()
	
		for index in indices_in_box:

			point = self.recorder.vertices[index,:]

			if neighbor_circle.is_point_inside(point):
				#print("yes, in the hood")

				dist_new = np.linalg.norm(point - self.new_v)
				dist_new = round(dist_new,6)

				self.neighbor_indices.append(index)
				self.neighbor_dist.append(dist_new)

		#print (self.neighbor_indices)
		#print (self.neighbor_dist)


	def find_indices_in_extents(self):
		"""fill out
		"""

		offset = self.neighbor_offset
		hx = [(self.new_v[0] - offset*self.params["neighborhood"]), (self.new_v[0] + offset*self.params["neighborhood"])]
		hy = [(self.new_v[1] - offset*self.params["neighborhood"]), (self.new_v[1] + offset*self.params["neighborhood"])]

		a = self.recorder.vertices[:,0] > hx[0]
		b = self.recorder.vertices[:,0] < hx[1]
		c = self.recorder.vertices[:,1] > hy[0]
		d = self.recorder.vertices[:,1] < hy[1]

		# indices of vertices found in bounding box
		indices_in_box =  [i for i, x in enumerate(a&b&c&d) if x]

		del indices_in_box[-1] #don't check last item since it's the new point itself

		return indices_in_box


	def find_parent_shortest_path(self):
		"""fill out
		"""

		#print(self.recorder.vertices)
		#print(self.recorder.parents)
		#print(self.recorder.costs)

		cost = 0.0
		lowest_cost = float('+inf') 

		for index,dist in zip(self.neighbor_indices, self.neighbor_dist):

			cost = self.update_path_cost(index,dist)
			print("\ncost to get from vertex",index, cost)

			if cost > lowest_cost:
				pass
			else:
				if not self.is_new_edge_blocked(self.new_v,self.recorder.vertices[index]):
					print("lower cost, parent is now",index)
					lowest_cost = cost
					new_parent_index = index
					new_parent_dist = dist

		print("new parent index", new_parent_index, "with cost", new_parent_dist)
		return new_parent_index, new_parent_dist


	def rewire(self,trial):
		"""fill out
		"""
		
		print("cost of vertex", trial, "is", self.recorder.costs[trial])
		for index,dist in zip(self.neighbor_indices, self.neighbor_dist):
			
			print("--to vertex:", index, self.recorder.costs[index], "is it more than", (self.recorder.costs[trial] + dist) )

			if (self.recorder.costs[trial] + dist) < self.recorder.costs[index]:

				print("do it....rewire index", self.recorder.parents[index], "to", trial )

				if not self.is_new_edge_blocked(self.new_v,self.recorder.vertices[index]):
					self.recorder.costs[index] = self.recorder.costs[trial] + dist
					self.recorder.parents[index] = trial


	def plot_tests(self,t1,t2,toggle):
		if toggle:
			Plot().simple_plot3(
				self.domain,
				self.recorder.parents,
				self.recorder.vertices,
				t1, t2
				)
			plt.pause(0.05)
