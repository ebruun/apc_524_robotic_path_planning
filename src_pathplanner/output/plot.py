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
                       'showlegend': False}

        self.fig = {'data': self.data,
                    'layout': self.layout}

	def plot_domain(self):
		"""  This function plots the shape of the domain.  """

		#TO DO...
		if self.dims == 2:  # plot in 2D 
		range_x = self.domain.extents[0]
		range_y = self.domain.extents[1]
		self.fig.update_xaxes(range=range_x)
		self.fig.update_yaxes(range=range_y)
		
		elif self.dims == 3: # plot in 3D
		range_x = self.domain.extents[0]
		range_y = self.domain.extents[1]
		range_z = self.domain.extents[2]
		self.fig.update_layout(scene = dict(aspectmode='data'))

		else: 
			print("Cannot plot in > 3 dimensions")
		
	def plot_obstacles(self):
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
				x = [goal[0] for goal in self.domain.goals],
				y = [goal[1] for goal in self.domain.goals],
				z = [goal[2] for goal in self.domain.goals],
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
			parents = [int(parent) for parent in solution.recorder.parents] 
			path_verts = solution.solution_path

			if self.dimensions == 2:  # plot in 2D
	            
	            #Plot entire graph
	            x, y = [], []
	            for i, parent in enumerate(parents):
					if parent < 0:
						continue
	                x.append(vertices[i, 0], vertices[parent, 0])
	                y.append(vertices[i, 1], vertices[parent, 1])
	            graph = go.Scatter(
	                x=x,
	                y=y,
	                line=dict(
	                    color="black",
	                    width=2
	                ),
	                mode="lines"
	            )
	            self.data.append(graph)

	            #Plot final path 
	            x2, y2 = [], []
	            for path in path_verts:
					if any(np.isnan(path)):
						continue			
					for i in path:
						if (parents[i] < 0):
							continue
						x2.append(vertices[i, 0], vertices[parent, 0])
		                y2.append(vertices[i, 1], vertices[parent, 1])
		            path = go.Scatter(
		                x=x2,
		                y=y2,
		                line=dict(
		                    color="red",
		                    width=4
		                ),
		                mode="lines"
		            )
		            self.data.append(path)
	        
	        elif X.dimensions == 3:  # plot in 3D
	            
	            #Plot entire graph
	            x, y, z = [], [], []
	            for i, parent in enumerate(parents):
					if parent < 0:
						continue
	                x.append(vertices[i, 0], vertices[parent, 0])
	                y.append(vertices[i, 1], vertices[parent, 1])
	 				z.append(vertices[i, 2], vertices[parent, 2])
				graph = go.Scatter3d(
	                x=x,
	                y=y,
	                z=z,
	                line=dict(
	                    color="black",
	                    width=2
	                ),
	                mode="lines"
	            )
	            self.data.append(graph)

	            #Plot final path 
	            x2, y2, z2 = [], [], []
	            for path in path_verts:
					if any(np.isnan(path)):
						continue			
					for i in path:
						if (parents[i] < 0):
							continue
						x2.append(vertices[i, 0], vertices[parents[i], 0])
		                y2.append(vertices[i, 1], vertices[parents[i], 1])
		                z2.append(vertices[i, 2], vertices[parents[i], 2])
		            path = go.Scatter(
		                x=x2,
		                y=y2,
		                z=z2,
		                line=dict(
		                    color="red",
		                    width=4
		                ),
		                mode="lines"
		            )
		            self.data.append(path)
	        
	        else:  # can't plot in higher dimensions
	            print("Cannot plot in > 3 dimensions")

	def set_axes(self):

		if self.dims == 2:  # plot in 2D 
		range_x = self.domain.extents[0]
		self.fig.update_layout(
			xaxis = dict(
				range = range_x,
				constrain = 'domain',
			),
		    yaxis = dict(
		    	scaleanchor = "x",
		    	scaleratio = 1,
		    ),
		)
		
		elif self.dims == 3: # plot in 3D
		range_x = self.domain.extents[0]
		range_y = self.domain.extents[1]
		range_z = self.domain.extents[2]
		self.fig.update_layout(scene = dict(aspectmode='data'))

		else: 
			print("Cannot plot in > 3 dimensions")

	def draw(self, auto_open=True):
        """
        Render the plot to a file
        """
        py.offline.plot(self.fig, filename=self.filename, auto_open=auto_open)

    def animate(self):
    	"""
        Animates the file with a simple play button
        """

