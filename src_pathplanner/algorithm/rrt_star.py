# rrt_star.py
# Author(s): Edvard Bruun

import numpy as np

from algorithm.rrt import RRT
from input.shape_circle import Circle

class RRT_Star(RRT):
	""" A class for RRT algorithm.

	"""

	def __init__(self,domain,recorder,params):
		super().__init__(domain,recorder,params)
		self.neighbor_indices = []
		self.neighbor_dist = []



	def rrt_step(self,trial):
		print("\nVertex", trial+1)
		
		self.new_q = self.new_config()
		self.new_v, self.new_parent, self.new_cost = self.new_vertex()

		if self.is_new_edge_blocked():
			self.rrt_step(trial)

		# New code for RRT_Star
		self.recorder.vertices[trial,:] = self.new_v

		#self.choose_parent()
		self.find_vertices_in_neighborhood()
		self.new_parent,self.new_cost = self.find_parent_shortest_path()

		self.recorder.parents[trial] = self.new_parent 
		self.recorder.costs[trial] = self.update_path_cost(self.new_parent,self.new_cost)

		#print(self.recorder.parents)
		#print(self.recorder.costs)



	def new_config(self):
		return super().new_config()

	def new_vertex(self):
		return super().new_vertex()

	def is_new_edge_blocked(self):
		return super().is_new_edge_blocked()

	def choose_parent(self):
		print("choose parent")
		new_parent_index, new_parent_dist = self.find_parent_shortest_path()

		return new_parent_index, new_parent_dist

	def find_vertices_in_neighborhood(self):
		"""fill out
		"""

		#print("verts in neighborhood")

		del self.neighbor_indices[:]
		del self.neighbor_dist[:]

		neighbor_circle = Circle({'radius':self.params.neighborhood, 'center':self.new_v})
		
		indices_in_box = self.find_indices_in_neighborhood()
	
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


	def find_indices_in_neighborhood(self):
		"""fill out
		"""

		offset = 1.05
		hx = [(self.new_v[0] - offset*self.params.neighborhood), (self.new_v[0] + offset*self.params.neighborhood)]
		hy = [(self.new_v[1] - offset*self.params.neighborhood), (self.new_v[1] + offset*self.params.neighborhood)]

		a = self.recorder.vertices[:,0] > hx[0]
		b = self.recorder.vertices[:,0] < hx[1]
		c = self.recorder.vertices[:,1] > hy[0]
		d = self.recorder.vertices[:,1] < hy[1]

		# indices of vertices found in bounding box
		indices_in_box =  [i for i, x in enumerate(a&b&c&d) if x]

		del indices_in_box[-1] #don't check last item since it's the new point itself

		return indices_in_box



	def find_parent_shortest_path(self):

		#print(self.recorder.vertices)
		#print(self.recorder.parents)
		#print(self.recorder.costs)

		cost = 0.0
		lowest_cost = float('+inf') 

		for index,dist in zip(self.neighbor_indices, self.neighbor_dist):

			cost = self.update_path_cost(index,dist)
			#print("cost", cost)

			if cost > lowest_cost and self.is_new_edge_blocked2(self.new_v,self.recorder.vertices[index]):
				pass
			else:
				#print("lower cost, parent is now",index)
				lowest_cost = cost
				new_parent_index = index
				new_parent_dist = dist

		return new_parent_index, new_parent_dist




