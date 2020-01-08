# plot1.py
# Author(s): Edvard Bruun

"""
Placeholder for the plotting class
"""

import matplotlib.pyplot as plt
import numpy as np

class Plot1():


	@classmethod
	def simple_plot1(cls, domain_object, parents, vertices, path_verts):
		fig, ax = plt.subplots()

		# ax.set_xlim([0, 3])
		# ax.set_ylim([0, 4])
		ax.set_aspect('equal')

		parents = [int(i) for i in parents]

		for i in range(len(parents)):
			if parents[i] < 0:
				continue
			plt.plot([vertices[i, 0], vertices[parents[i], 0]], 
					 [vertices[i, 1], vertices[parents[i], 1]], c='k')

			
		for path in path_verts:

			if any(np.isnan(path)):
				#print("nan")
				continue			

			for i in path:

				if (parents[i] < 0):
					#print("end")
					continue

				plt.plot([vertices[i, 0], vertices[parents[i], 0]], 
						 [vertices[i, 1], vertices[parents[i], 1]], c='r')    


		for o in domain_object.obstacles:
			ax.add_artist(plt.Circle(tuple(np.asarray(o.center)), o.radius))


		for goal in domain_object.goals:
			ax.add_artist(plt.Circle(tuple(np.asarray(goal.center)), goal.radius,
				ec=(0.004, 0.596, 0.105),
				fc=(1, 1, 1)))

			plt.scatter(goal.center[0], goal.center[1],
				zorder=3,
				c=np.array([[0.004, 0.596, 0.105]]),
				s=30)

		plt.scatter(domain_object.origin[0], domain_object.origin[1],
			zorder=3,
			c=np.array([[0.004, 0.596, 0.105]]),
			s=30)

		for path in path_verts:

			if any(np.isnan(path)):
				#print("nan")
				continue

				plt.scatter(
					vertices[path, 0],
					vertices[path, 1],
					c=np.array([[1, 0, 0]]),
					s=3,
					zorder=2)

		plt.scatter(
			vertices[0:, 0],
			vertices[0:, 1],
			c=np.array([[0, 0, 0]]),
			s=7)

		plt.show()


	@classmethod
	def simple_plot2(cls, domain_object):
		fig, ax = plt.subplots()

		ax.set_xlim([0, 3])
		ax.set_ylim([0, 4])

		ax.set_aspect('equal')	
		plt.plot([1,2,3,4])
		plt.show() 


	@classmethod
	def simple_plot3(cls, domain_object, parents, vertices, trial_path, trial_vert):
		fig, ax = plt.subplots()

		ax.set_xlim([0, 3])
		ax.set_ylim([0, 4])
		ax.set_aspect('equal')

		parents = [int(i) for i in parents[0:trial_path]]

		for i in range(trial_path):
			if parents[i] < 0:
				continue
			plt.plot([vertices[i, 0], vertices[parents[i], 0]], 
					 [vertices[i, 1], vertices[parents[i], 1]], c='k')
 


		for o in domain_object.obstacles:
			ax.add_artist(plt.Circle(tuple(o.center), o.radius))


		for goal in domain_object.goals:
			ax.add_artist(plt.Circle(tuple(goal.center), goal.radius,
				ec=(0.004, 0.596, 0.105),
				fc=(1, 1, 1)))

			plt.scatter(goal.center[0], goal.center[1],
				zorder=3,
				c=np.array([[0.004, 0.596, 0.105]]),
				s=30)

		plt.scatter(domain_object.origin[0], domain_object.origin[1],
			zorder=3,
			c=np.array([[0.004, 0.596, 0.105]]),
			s=30)


		plt.scatter(
			vertices[0:(trial_vert), 0],
			vertices[0:(trial_vert), 1],
			c=np.array([[0, 0, 0]]),
			s=7)

		plt.show()