# plot.py
# Author(s): Jessica Flores

"""
Plotting class
"""

import numpy as np
import plotly.express as px

from plotly import graph_objs as go

class Animate:
	""" A class to plot the domain, obstacles, start and end points, as well as 
		optionally the solution graph of the path planning algorithm.	
	"""
	
	def __init__(self, filename, domain):
		"""
		Initializes the plot 
		:param filename: filename for plot html
		:type filename: string

		"""
		self.filename = "./output/" + filename + ".html"
		self.title = filename
		self.domain = domain
		self.dims = domain.dims

		self.fig = go.Figure()
		
	def plot_obstacles(self):
		"""  This function plots the obstacles in the domain.  """
		
		if self.dims == 2:
			
			for obstacle in self.domain.obstacles:
				self.fig.add_shape(
					go.layout.Shape(
						type = obstacle[0],
						xref="x",
						yref="y",
						fillcolor="blue",
						x0=obstacle[1][0]-obstacle[2],
						y0=obstacle[1][1]-obstacle[2],
						x1=obstacle[1][0]+obstacle[2],
						y1=obstacle[1][1]+obstacle[2],
						line_color="blue"
				))
		else:
			pass 

	def plot_origin_goals(self):
		"""  This function plots the origin point and goal points/shapes.  """

		if self.dims == 2:
			self.fig.add_trace(go.Scatter(
				x = [self.domain.origin[0]],
				y = [self.domain.origin[1]],
				line=dict(
					color="orange",
					width=10
				),
				mode="markers",
				showlegend=False
			))

			#plot goal point (optional?)
			# self.fig.add_trace(go.Scatter(
			# 	x = [goal[1][0] for goal in self.domain.goals],
			# 	y = [goal[1][1] for goal in self.domain.goals],
			# 	line=dict(
			# 	color="green",
			# 	width=10
			# 	),
			# 	mode="markers",
			# 	showlegend=False
			# ))

			for goal in self.domain.goals:
				self.fig.add_shape(
					go.layout.Shape(
						type = goal[0],
						xref="x",
						yref="y",
						x0=goal[1][0]-goal[2],
						y0=goal[1][1]-goal[2],
						x1=goal[1][0]+goal[2],
						y1=goal[1][1]+goal[2],
						line_color="green"
				))

			# self.fig.add_shape(
			# 	go.layout.Shape(
			# 			type="path",
			# 			path="M 0,9 1\
			# 				C 1,1 0,9 1 0,7 1,2 0,6\
			# 				C 1,4 0,5 1,9 0.7 2 1,1\
			# 				c 0 0,2 -0,1 0,5 -0,2 0,5\
			# 				c -0,2 0 -0,3 -0,3 -0,6 -0,4\
			# 				c -0,3 0 -0,4 0,2 -0,6 0,2\
			# 				C 0,4 1,3 0,3 0,9 0,5 0,9\
			# 				C 0,6 0,8 0,7 1 0,9 1z",
			# 			line_color="MediumPurple"
			# 	))

		elif self.dims == 3:
			origin = go.Scatter(
				x = [domain.origin[0]],
				y = [domain.origin[1]],
				z = [domain.origin[2]],
				line=dict(
					color="orange",
					width=10
				),
				mode="markers",
				showlegend=False
			)
			self.data.append(origin)

			goals = go.Scatter(
				x = [goal[1][0] for goal in self.domain.goals],
				y = [goal[1][1] for goal in self.domain.goals],
				z = [goal[1][2] for goal in self.domain.goals],
				line=dict(
					color="green",
					width=10
				),
				mode="markers",
				showlegend=False
			)
			self.data.append(goals)

		else:  
			print("Cannot plot in > 3 dimensions")

	def plot_solution_graph(self, solution=None):
		"""  This function plots the solution graph if given. """
		if solution == None:
			print("provide solution object as argument")

		else:
			vertices = solution.recorder.vertices 
			parents = [int(parent) for parent in solution.recorder.parents] 
			path_verts = solution.solution_path

			if self.dims == 2:  # plot in 2D
				
				#Plot entire graph
				for i, parent in enumerate(parents):
					if parent < 0:
						continue
					self.fig.add_trace(go.Scatter(
						x=[vertices[i, 0],vertices[parent, 0]],
						y=[vertices[i, 1],vertices[parent, 1]],
						line=dict(
							color="black",
							width=2
						),
						mode='lines+markers',
						showlegend=False
					))
				
				for i, parent in enumerate(parents):
					if parent < 0:
						continue
					self.fig.add_trace(go.Scatter(
						x=[vertices[i, 0],vertices[parent, 0]],
						y=[vertices[i, 1],vertices[parent, 1]],
						line=dict(
							color="black",
							width=2
						),
						mode='lines+markers',
						showlegend=False
					))
				frames = [dict(data= [dict(type='scatter',
				                           x=df.Date[:k+1],
				                           y=low[:k+1])],
						               traces= [0],
						              )for k  in  range(1, len(low)-1)] 

				#Plot final path 
		
				for path in path_verts:
					if any(np.isnan(path)):
						continue
					for i in path:
						if (parents[i] < 0):
							continue
						self.fig.add_trace(go.Scatter(
							x=[vertices[i, 0], vertices[parents[i], 0]],
							y=[vertices[i, 1], vertices[parents[i], 1]],
							line=dict(
								color="red",
								width=4
							),
							mode='lines+markers',
							showlegend=False
						))
						
			
			elif self.dims == 3:  # plot in 3D
				
				#Plot entire graph
				x, y, z = [], [], []
				for i, parent in enumerate(parents):
					if parent < 0:
						continue
					x.append(vertices[i, 0])
					x.append(vertices[parent, 0])
					y.append(vertices[i, 1])
					y.append(vertices[parent, 1])
					z.append(vertices[i, 2])
					z.append(vertices[parent, 2])
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
						x2.append(vertices[i, 0])
						x2.append(vertices[parents[i], 0])
						y2.append(vertices[i, 1])
						y2.append(vertices[parents[i], 1])
						z2.append(vertices[i, 2])
						z2.append(vertices[parents[i], 2])
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

	def set_layout(self):

		self.fig.update_layout(
				title=self.title)

		if self.dims == 2:  # plot in 2D 
			range_x = self.domain.extents[0]
			self.fig.layout.update(
				xaxis = dict(
					range = range_x,
					constrain = 'domain',
				),
				yaxis = dict(
					scaleanchor = "x",
					scaleratio = 1,
				),
				showlegend=False,
				hovermode='closet',
				updatemenus=[dict(type='buttons', showactive=False,
                                y=1.05,
                                x=1.15,
                                xanchor='right',
                                yanchor='top',
                                pad=dict(t=0, r=10),
                                buttons=[dict(label='Play',
                                              method='animate',
                                              args=[None, 
                                                    dict(frame=dict(duration=3, 
                                                                    redraw=False),
                                                         transition=dict(duration=0),
                                                         fromcurrent=True,
                                                         mode='immediate')])])]
			)
			self.fig.update_yaxes(range=self.domain.extents[1])
		
		elif self.dims == 3: # plot in 3D
			# range_x = self.domain.extents[0]
			# range_y = self.domain.extents[1]
			# range_z = self.domain.extents[2]
			self.fig.layout.update(scene = dict(aspectmode='data'))

		else: 
			print("Cannot plot in > 3 dimensions")

	def draw(self, auto_open=True):
		"""
		Render the plot to a file
		"""
		py.offline.plot(self.fig, filename=self.filename, auto_open=auto_open)



