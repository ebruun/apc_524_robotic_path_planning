# PathPlan.py
# Author(s): Edvard Bruun

# Main file for Path Planning Program

from rrt.solver import *

# Code for reading in data

#Algorithm code
RRT = Solver(2)
RRT.solve_rrt()

# Code for visualizing and presenting results
