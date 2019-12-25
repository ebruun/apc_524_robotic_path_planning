# PathPlan.py
# Author(s): Edvard Bruun

# Main file for Path Planning Program

from rrt.solver import Solver

from input.params import ParamsRRT
from input.params import ParamsOriginGoal
from input.params import ParamsDomain


# Code for reading in data
input_file = "parameters.txt"

#Algorithm code
RRT = Solver(ParamsRRT(input_file))

RRT.solve_rrt()
RRT.check_completion()


# Code for visualizing and presenting results
