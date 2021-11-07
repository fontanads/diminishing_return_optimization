from ortools.linear_solver import pywraplp
from ortools.init import pywrapinit

import numpy as np

def main():
    # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Create the variable x
    x = solver.NumVar(1e-3, 1e6, 'x')

    print('Number of variables =', solver.NumVariables())

    # some constraint parameter
    R = 50

    # some linear coefficient
    a = 10

    # Create a linear constraint,  0 < 1*x <= a/r 
    lb_x = 1e-3     # lower bound on x
    ub_x = a/R      # upper bound on x
    ct = solver.Constraint(lb_x, ub_x, 'ct')
    ct.SetCoefficient(x, 1)

    print('Number of constraints =', solver.NumConstraints())

    # Create the objective function, f(x) = a * log(x)
    objective = solver.Objective()
    objective.SetCoefficient(np.log(x), a)
    objective.SetMaximization()

    solver.Solve()

    print('Solution:')
    print('Objective value =', objective.Value())
    print('x =', x.solution_value())


if __name__ == '__main__':
    print("I passed here.")
    pywrapinit.CppBridge.InitLogging('basic_example.py')
    cpp_flags = pywrapinit.CppFlags()
    cpp_flags.logtostderr = True
    cpp_flags.log_prefix = False
    pywrapinit.CppBridge.SetFlags(cpp_flags)

    main()

main()