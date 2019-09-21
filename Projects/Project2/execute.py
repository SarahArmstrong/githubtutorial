'''
This file is a script that solves for the steady-state in the two-
period-lived overlapping generations model given some parameter values.
'''

# Put import commands below here


# Set parameter values

# Household parameters
n1       = 1.0
n2       = 0.2
nvec     = np.array([n1, n2])
gamma    = 2.2
beta_an  = 0.96
beta     = beta_an ** (30) 

# Firm parameters
A        = 1.0
alpha    = 0.33
delta_an = 0.05
delta    = 1 - (1 - delta_an) ** (1/30)


# Solve for b2 given parameters




# Solve for all the other endogenous variables given parameter values
# and optimal b2




# Print steady-state equilibrium endogenous variables
