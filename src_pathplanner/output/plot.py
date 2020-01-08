# plot.py
# Author(s): Jessica Flores

"""
Plotting class
"""

import numpy as np
import plotly as py

from plotly import graph_objs as go
from PIL import Image

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
		self.filename = "./output/" + filename + ".html"
		self.title = filename
		self.domain = domain
		self.dims = domain.dim

		self.fig = go.Figure()
		
	def plot_obstacles(self):
		"""  This function plots the obstacles in the domain.  """
		
		if self.dims == 2:
			
			for i,obstacle in enumerate(self.domain.obstacles):
				if obstacle.name == "circle":
					center = obstacle.center
					x_min = center[0]-obstacle.radius
					x_max = center[0]+obstacle.radius
					y_min = center[1]-obstacle.radius
					y_max = center[1]+obstacle.radius
					self.fig.add_shape(
						go.layout.Shape(
							type = "circle",
							xref="x",
							yref="y",
							fillcolor="blue",
							x0=x_min,
							y0=y_min,
							x1=x_max,
							y1=y_max,
							line_color="blue",
							opacity=0.5,
					))
				elif obstacle.name == "rectangle":
					ll_corner = obstacle.ll_corner
					ur_corner = obstacle.ur_corner
					extents = [[ll_corner[0],ur_corner[0]],[ll_corner[1],ur_corner[1]]]
			
					self.fig.add_shape(
						go.layout.Shape(
							type = "rect",
							xref="x",
							yref="y",
							fillcolor="blue",
							x0=ll_corner[0],
							y0=ll_corner[1],
							x1=ur_corner[0],
							y1=ur_corner[1],
							line_color="blue",
							opacity=0.5,
					))
				elif obstacle.name == "free_form":
					img = Image.open(obstacle.file)
					img.save('obstacle'i'.png')
					png_img = Image.open('obstacle'i'.png')
					self.fig.add_layout_image(
						dict(
							source=png_img,
							xref="x",
							yref="y",
							x=obstacle.x_min_val,
							y=obstacle.y_max_val,
							))

				else:
					raise Exception('The obstacle shape is not implemented')

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
				if goal.name == "circle":
					center = goal.center
					x_min = center[0]-goal.radius
					x_max = center[0]+goal.radius
					y_min = center[1]-goal.radius
					y_max = center[1]+goal.radius
					self.fig.add_shape(
						go.layout.Shape(
							type = "circle",
							xref="x",
							yref="y",
							fillcolor="green",
							x0=x_min,
							y0=y_min,
							x1=x_max,
							y1=y_max,
							line_color="green",
							opacity=0.5,
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
				
				#self.data.append(graph)

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
			
			if self.domain.domain_shape == "circle":
				center = self.domain.domain.center
				print(center)
				print(self.domain.domain.radius)
				x_min = center[0]-self.domain.domain.radius
				print(x_min)
				x_max = center[0]+self.domain.domain.radius
				y_min = center[1]-self.domain.domain.radius
				y_max = center[1]+self.domain.domain.radius
				self.fig.add_shape(
					go.layout.Shape(
						type = "circle",
						xref="x",
						yref="y",
						x0=x_min,
						y0=y_min,
						x1=x_max,
						y1=y_max,
						line=dict(
			                color="Black",
			                width=15
        				)
				))
				extents = [[x_min,x_max],[y_min,y_max]]

			elif self.domain.domain_shape == "rectangle":
				ll_corner = self.domain.domain.ll_corner
				ur_corner = self.domain.domain.ur_corner
				extents = [[ll_corner[0],ur_corner[0]],[ll_corner[1],ur_corner[1]]]
			
			range_x = extents[0]
			self.fig.layout.update(
				xaxis = dict(
					range = range_x,
					constrain = 'domain',
				),
				yaxis = dict(
					scaleanchor = "x",
					scaleratio = 1,
				),
			)
			self.fig.update_yaxes(range=extents[1])
		
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

	def animate_solution_graph(self, solution=None):
		"""
		Animates the file with a simple play button
		"""
		if solution == None:
			pass

		else:
			vertices = solution.recorder.vertices 
			parents = [int(parent) for parent in solution.recorder.parents] 
			path_verts = solution.solution_path

			if self.dims == 2:  # plot in 2D
				
				#Plot entire graph
				for i, parent in enumerate(parents):
					if parent < 0:
						continue
					self.fig.add_frames(go.Scatter(
						x=[vertices[i, 0],vertices[parent, 0]],
						y=[vertices[i, 1],vertices[parent, 1]],
						line=dict(
							color="black",
							width=2
						),
						mode='lines+markers',
						showlegend=False
					))
				

				#Plot final path 
		
				for path in path_verts:
					if any(np.isnan(path)):
						continue
					for i in path:
						if (parents[i] < 0):
							continue
						self.fig.add_frames(go.Scatter(
							x=[vertices[i, 0], vertices[parents[i], 0]],
							y=[vertices[i, 1], vertices[parents[i], 1]],
							line=dict(
								color="red",
								width=4
							),
							mode='lines+markers',
							showlegend=False
						))

			else:
				pass

