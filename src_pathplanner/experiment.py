from input.domain import Domain

from algorithm.rrt_basic import RRT_Basic

from input.params import ParamsRRT
from input.params import ParamsOriginGoal
from input.params import ParamsDomain


print("1. Parameters")
input_file = "parameters.txt"

p1 = ParamsRRT(input_file)
p2 = ParamsDomain(input_file)
p3 = ParamsOriginGoal(input_file)

print("2. Create Domain")
d1 = Domain(p2,p3)

a = RRT_Basic(d1)

print(a.domain.goal)

a.new_vertex()