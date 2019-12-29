# stepper.py
# Author(s): Edvard Bruun

import numpy as np

from solver.recorder import Recorder
from solver.stepper import Stepper


class Solution:
	"""This class executes and saves the solution to the path planning problem.

	Imports the :class:`solver.stepper` module

	Imports the :class:`solver.recorder` module

	"""

	def __init__(self,params,domain):
		"""Initialize the Solution class.

		Note:
			Input parameters are assigned to instance variables with same name.

		Args:
			params (:obj:`input.params.ParamsRRT`):
				Object containing the algorithm parameters
			domain (:obj:`input.domain`):
				Object containing the assembled solution domain

		Attributes:
			recorder (:obj:`solver.recorder`):
				initialized recorder object with parameters
			stepper (:obj:`solver.stepper`):
				initialized stepper object with parameters		
			solution_path (:obj:`list` of :obj:`list` of :obj:`int`):
				a path from origin to each goal in the form of vertex indices.
			solution_index (:obj:`list` of :obj:`int`):
				index for final vertex to reach each goal.
		
		"""

		self.params = params
		self.domain = domain

		self.recorder = Recorder(params)
		self.stepper = Stepper(params)

		self.solution_path = [] 
		self.solution_index = []

	def run_algorithm(self):
		"""  This function runs through all the iterations of the solution algorithm.

		"""

		for trial in range(self.params.n_trials):
			print("\nIteration # ", trial+1)
			self.stepper.do_singlestep(self.recorder, trial)


	def check_completion(self):
		"""  This function checks the final list of vertices calculated by the algorithm
		against the set of established goals.

		Saves an index that represents the vertex that has reached the goal.

		"""

		for i in range(len(self.domain.goal)):
			index = self.check_if_goal_reached(self.domain.goal[i])

			self.solution_index.append(index)

		self.find_path_backtrack()

		
	def check_if_goal_reached(self,goal):
		"""  This function checks if a single goal has been reached.

		Goal - currently in the form ["string", middle point, radius]

		distance is measured from the center of the goal object,
		and its perimeter is the outer edge

		change this to .isinside(point) function once the goal is defined as a shape

		Returns::

			index -- Goal Reached.
			nan -- Goal Not Reached.

		"""

		index, distance = self.find_nearest_vertex(goal[1])

		print("--Shortest distance:", distance, ", Found with vertex at index:", index)

		if (distance < goal[2]):
			print('Path found!')
			return index
		else:
			print('No path found!')
			return np.nan


		

	def find_nearest_vertex(self,goal):
		"""  This function finds how far the closest vertex is to the center of goal.

		:arg goal: The center of the object specified as a goal
		:type goal: shape object

		:param goal: The center of the object specified as a goal
		:type goal: shape object

		Returns::

			index of nearest vertex to the specified goal

			distance from nearest vertex to specified goal

		"""
		dist_new = 0
		shortest_distance = float('+inf') #Initialize large number for first distance comparison
		shortest_index = 0
		
		for i, vertex in enumerate(self.recorder.vertices):

			if any(x == True for x in np.isnan(vertex)):
				print("--Looked through all current vertices")
				break
			else:
				dist_new = np.linalg.norm(goal - vertex)
				
				if dist_new < shortest_distance:					
					shortest_distance = dist_new
					shortest_index = i
		
		return shortest_index, shortest_distance



	def find_path_backtrack(self):
		"""  This function finds the sequence of nodes working back from a specifed vertex
		to the starting origin

		For each goal a path backwards, as a list of vertex indices, is saved as a list

		"""
		for i, index in enumerate(self.solution_index):

			path_list = []
			path_list.append(index) #Index of closest vertex to the goal
			child = index

			# Loop through parents list until you reach parents[i] = '-1',
			# which is the starting point (no parent)
			while child > 0:
				print("hre")
				parent = int(self.recorder.parents[child])
				path_list.append(parent)
				
				child = parent #Set the parent index, as the child for next loop
			
			path_list.reverse()		

			self.solution_path.append(path_list)








