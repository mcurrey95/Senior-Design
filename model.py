#model goes here


import pulp
import random

prob = pulp.LpProblem("Truck Driver Scheduling", pulp.LpMinimize)

NUMBER_OF_DRIVERS = 32

DRIVERS = [i for i in range(NUMBER_OF_DRIVERS)]  # TODO: MAKE A FUNCTION TO GET THIS NUMBER
SHIFTS = [day for day in range(14)]


# Decision Variables
x = {i: {j: pulp.LpVariable('x({})({})'.format(i, j), cat=pulp.LpBinary) for j in SHIFTS} for i in DRIVERS}

# Intermediaries
Delta = pulp.LpVariable("delta", lowBound=0, cat=pulp.LpInteger)
R = {i:pulp.LpVariable("R{}".format(i), lowBound=0, cat=pulp.LpInteger) for i in DRIVERS}
Rt = {i:pulp.LpVariable("Rt{}".format(i), lowBound=0, cat=pulp.LpInteger) for i in DRIVERS}
Z = {i:pulp.LpVariable("Z{}".format(i), lowBound=0, cat=pulp.LpBinary) for i in DRIVERS}
Zt = {i:pulp.LpVariable("Zt{}".format(i), lowBound=0, cat=pulp.LpBinary) for i in DRIVERS}
Q = {i:pulp.LpVariable("Q{}".format(i), lowBound=0,cat=pulp.LpInteger) for i in DRIVERS}

#Parameters
#TODO: GET RID OF THE RANDOM PARTS OF PARAMETERS
c = {i: {j: random.randint(0, 1) for j in SHIFTS} for i in DRIVERS}
D = {m: random.randint(1000,2000) for m in range(7)}
K = {i: 5 for i in DRIVERS}
T = {j: 4 for j in SHIFTS}
DP = 1000000
MSC = 100
