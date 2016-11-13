#model goes here


import pulp

prob = pulp.LpProblem("Truck Driver Scheduling", pulp.LpMinimize)

NUMBER_OF_DRIVERS = 32

DRIVERS = [i for i in range(NUMBER_OF_DRIVERS)] #TODO: MAKE A FUNCTION TO GET THIS NUMBER
SHIFTS = [day for day in range(14)]


# class pulp.LpVariable(name, lowBound=None, upBound=None, cat='Continuous', e=None)
DecisionVariables = {i: {j: pulp.LpVariable('x({})({})'.format(i, j), cat=pulp.LpBinary) for j in SHIFTS} for i in DRIVERS}

#