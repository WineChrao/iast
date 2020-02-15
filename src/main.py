#
# Ideal Adsorbed Solution Theory for binary mixture using Langmuir isotherms
#

import numpy as np

from collections import namedtuple
from iast import iast
from fit_isotherm import fitIsotherm

file_name1 = "Results.dat-ZIF-8-433K-methane"
file_name2 = "Results.dat-ZIF-8-433K-ethane"

isotherm_type = 0
n_components = 2
y1 = 0.5
pressure_initial = 1e5
pressure_final = 2e6
n_pressure_intervals = 20
d_pressure = (pressure_final - pressure_initial) / (n_pressure_intervals - 1)
isotherm_parameters = fitIsotherm(isotherm_type, file_name1, file_name2)

Parameters = namedtuple('parameter', ['pressure_initial',
                                      'isotherm_parameters', 'y',
                                      'n_components', 'isotherm_type'])
S = Parameters(pressure_initial, isotherm_parameters, np.array([y1, 1-y1]),
               n_components, isotherm_type)

print("# pressure (Pa), loading 1, loading 2")
for i in range(n_pressure_intervals):
    P = S.pressure_initial + (i * d_pressure)
    q = iast(P, S)
    print(P, q)