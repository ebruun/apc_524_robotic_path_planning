# solution.py
# Author(s): Edvard Bruun

"""
Imports the :class:`solver.stepper.Stepper` class

Imports the :class:`solver.recorder.Recorder` class
"""

import numpy as np

from solver.recorder import Recorder
from solver.stepper import Stepper


class Solution:
	"""This class executes and saves the solution to the path planning problem.

	"""

	def __init__(self,params,domain):
		"""Initialize the Solution class.

		The intialization consists of creating new Recorder and Stepper objects, which are initialized based on the params object.

		Note:
			The input parameters are assigned to instance variables with same name.

		Parameters:
			params (:obj:`~input.params.ParamsRRT` object):
				Object containing the algorithm parameters.
			domain (:obj:`~input.domain.Domain` object):
				Object containing the assembled solution domain.

		Attributes:
			params: see Parameters
			domain: see Parameters
			recorder (:class:`~solver.recorder.Recorder` object):
				Initialized recorder object with input parameters.
			stepper (:obj:`~solver.stepper.Stepper` object):
				Initialized stepper object with input parameters.	
			solution_path (:obj:`list` of :obj:`list` of :obj:`int`):
				A path from origin to each goal in the form of vertex indices. A single path is generated for each goal.
		
		"""
		self.params = params
		self.domain = domain

		self.recorder = Recorder(params)
		self.stepper = Stepper(params)

		self.solution_path = [] 


	def run_algorithm(self):
		"""  This function runs through the full algorithm.

		A single trial of the algorithm is executed in each iteration of the loop called in this function. The maximum number of trials is specified in the :obj:`~input.params.ParamsRRT` object.

		Calls the :meth:`stepper.do_singlestep() 
		<solver.stepper.Stepper.do_singlestep>` function in the loop.

		"""
		for trial in range(self.params.n_trials):
			#print("\nIteration # ", trial+1)
			self.stepper.do_singlestep(self.recorder, self.domain, trial)
			

	def process_vertex_list(self):
		"""  This function post-processes the full vertex list resulting from  completing the algorithm.

		Loop iterations based on number of goals to evaluate against.

		Calls the :meth:`~solver.solution.Solution.check_if_goal_reached` function in the loop. Returns the index of the vertex to reach the goal.

		Calls the :meth:`~solver.solution.Solution.find_path()` function in the loop. Finds the path from the origin to the vertex to reach the goal.

		"""
		for i in range(len(self.domain.goal)):
			index = self.check_if_goal_reached(self.domain.goal[i])
			self.solution_path.append(self.find_path(index))


	def check_if_goal_reached(self,goal):
		"""  This function checks if a single goal has been reached.

		Calls the :meth:`~solver.solution.Solution.find_nearest_vertex()` function to find the index of the closest vertex and its distance to the center of the goal.

		Checks to see if the closest vertex is within the boundary (perimeter) of the goal object. If it is within the boundary then the goal is reached.

		Error:
			TO DO:
			Goal - currently in the form ["string", middle point, radius]

			distance is measured from the center of the goal object, and its perimeter is the outer edge

			Change this check to .isinside(point) function once the goal is defined as a shape

		Parameters:
			goal (:obj:`~input.shape.Shape` object): A shape object specfied as the target for the algorithm.	

		Returns:
			index (:obj:`int`): The index of the vertex that reached the goal. This is set to :obj:`numpy.nan` if the goal is not reached.

		"""
		index, distance = self.find_nearest_vertex(goal[1])

		#print("--Shortest distance:", distance,", Found with vertex at index:", index)

		if (distance < goal[2]):
			#print('Path found!')
			return index
		else:
			#print('No path found!')
			index = np.nan
			return index


	def find_nearest_vertex(self,goal):
		"""  This function finds how far the nearest vertex is to a goal.

		The full list of vertices, saved in the :obj:`~solver.recorder.Recorder` object, is checked against a single goal target. Loops through the full list and calculates the L2 norm to the center of the goal. Updates the index and distance for the closest vertex through the loop.

		Parameters:
			goal (:obj:`~input.shape.Shape` object): A shape object specfied as the target for the algorithm.

		Returns:
			(tuple): tuple containing:

				shortest_index (:obj:`int`): The index of the vertex that is closest to the goal.

				shortest_distance (:obj:`float`): The distance from the closest vertex to the center point of the object

		Error:
			TO DO:
			Don't need to return the distance once the .isinside() function is created for the goal objects

		"""
		dist_new = 0.0
		shortest_distance = float('+inf') 
		shortest_index = 0
		
		for i, vertex in enumerate(self.recorder.vertices):

			if any(x == True for x in np.isnan(vertex)):
				break
			else:
				dist_new = np.linalg.norm(goal - vertex)
				dist_new = round(dist_new,6)
				
				if dist_new < shortest_distance:					
					shortest_distance = dist_new
					shortest_index = i
		
		return shortest_index, shortest_distance


	def find_path(self,index):
		"""  This function creates a path of indices from the origin to the end vertex.

		Finds the sequence of nodes working back from a specifed vertex index to the starting origin using the values in the parents list, saved in the :obj:`~solver.recorder.Recorder` object.

		The list of vertex indices for the full path is appended to the :attr:`solution_path` list of lists.
		
		Note:
			Parent of vertex i is j, then parents[i] == j

			For the origin vertex, parents[0] == -1

		"""
		path_list = []
		path_list.append(index)
		child = index

		while child > 0:
			parent = int(self.recorder.parents[child])
			path_list.append(parent)
			
			child = parent #Set the parent index, as the child for next loop
		
		path_list.reverse()		

		return path_list

