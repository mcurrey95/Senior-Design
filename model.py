#model goes here


import pulp

prob = pulp.LpProblem("Truck Driver Scheduling", pulp.LpMinimize)

NUMBER_OF_DRIVERS = 32

DRIVERS = [i for i in range(NUMBER_OF_DRIVERS)] #TODO: MAKE A FUNCTION TO GET THIS NUMBER
SHIFTS = [day for day in range(14)]


# class pulp.LpVariable(name, lowBound=None, upBound=None, cat='Continuous', e=None)
DecisionVariables = {i: {j: pulp.LpVariable('x({})({})'.format(i, j), cat=pulp.LpBinary) for j in SHIFTS} for i in DRIVERS}

Delta = pulp.LpVariable("delta", lowBound=0, cat=pulp.LpInteger)
R = {i:pulp.LpVariable("R{}".format(i), lowBound=0, cat=pulp.LpInteger) for i in DRIVERS}
Rt = {i:pulp.LpVariable("Rt{}".format(i), lowBound=0, cat=pulp.LpInteger) for i in DRIVERS}
Z = {i:pulp.LpVariable("Z{}".format(i), lowBound=0, cat=pulp.LpBinary) for i in DRIVERS}
Zt = {i:pulp.LpVariable("Zt{}".format(i), lowBound=0, cat=pulp.LpBinary) for i in DRIVERS}
Q = {i:pulp.LpVariable("Q{}".format(i), lowBound=0,cat=pulp.LpInteger) for i in DRIVERS}
