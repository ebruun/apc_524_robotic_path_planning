# planpath.py
# Author(s): Edvard Bruun

"""
planpath.py
====================================
The core module of the project, executes the program
"""


from solver.solution import Solution

from input.params import ParamsRRT
from input.params import ParamsOriginGoal
from input.params import ParamsDomain


# Code for reading in data
input_file = "parameters.txt"

#Algorithm code
RRT = Solution(ParamsRRT(input_file))

RRT.algorithm_step()
RRT.check_completion()


# Code for visualizing and presenting results
