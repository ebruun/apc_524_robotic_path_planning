# plot.py
# Author(s): Jessica Flores

"""
Plotting class
"""

import numpy as np
import plotly as py

from plotly import graph_objs as go
from solver.solution import Solution

class Plot:
	""" A class to plot the domain, obstacles, start and end points, as well as 
		optionally the solution graph of the path planning algorithm.	
	"""
	
	def __init__(self, filename, domain):
		"""
        Initializes the plot 
        :param filename: filename for plot html
        :type filename: string

        """
		self.filename = "../../output/visualizations/" + filename + ".html"
        self.domain = domain
        self.dims = domain.dims

		self.data = []
        self.layout = {'title': 'Plot',
                       'showlegend': False
                       }

        self.fig = {'data': self.data,
                    'layout': self.layout}

	def plot_domain(self, domain):
		"""  This function plots the shape of the domain.  """

		#TO DO...
		if self.dims == 2:  # plot in 2D 

		elif self.dims == 3: # plot in 3D

		else: 
			print("Cannot plot in > 3 dimensions")
		
	def plot_obstacles(self, domain):
		"""  This function plots the obstacles in the domain.  """
		
		#TO DO... 

	def plot_origin_goals(self):
		"""  This function plots the origin and goal points.  """

		if self.dims == 2:
			origin = go.Scatter(
				x = [self.domain.origin[0]],
				y = [self.domain.origin[1]],
				line=dict(
                    color="orange",
                    width=10
                ),
                mode="markers"
            )
            self.data.append(origin)

           	goals = go.Scatter(
				x = [goal[0] for goal in self.domain.goals],
				y = [goal[1] for goal in self.domain.goals],
				line=dict(
                color="green",
                width=10
               	),
               	mode="markers"
           	)
            self.data.append(goals)

        elif self.dims == 3:
			origin = go.Scatter(
				x = [domain.origin[0]],
				y = [domain.origin[1]],
				z = [domain.origin[2]],
				line=dict(
                    color="orange",
                    width=10
                ),
                mode="markers"
            )
            self.data.append(origin)

            goals = go.Scatter(
				x = [domain.goals[0]],
				y = [domain.goals[1]],
				z = [domain.goals[2]],
				line=dict(
                    color="green",
                    width=10
                ),
                mode="markers"
            )
            self.data.append(goals)

        else:  
            print("Cannot plot in > 3 dimensions")

	def plot_solution_graph(self, solution=None):
		"""  This function plots the solution graph if given. """
		if solution = None:
			pass

		else:

			vertices = solution.recorder.vertices 
			parents = solution.recorder.parents 
			solution_path = solution.solution_path

	 def draw(self, auto_open=True):
        """
        Render the plot to a file
        """
        py.offline.plot(self.fig, filename=self.filename, auto_open=auto_open)

    def animate(self):
    	"""
        Animates the file with a simple play button
        """

