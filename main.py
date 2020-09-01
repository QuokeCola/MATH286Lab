from Euler_Method import *
from Opt_Euler_Method import *
from RungKutta_Method import *

import matplotlib.pyplot as plt
import numpy as np

def diffF(x,y):
    return 1 - x + 4 * y

start_Point = (0,1)
end_Scale = 10
Step = 0.025

euler = Euler(diffF, Step, start_Point, end_Scale)
optEu = OptEu(diffF, Step, start_Point, end_Scale)
runKu = RunKu(diffF, Step, start_Point, end_Scale)
EulRes = euler.compute()
OptEuRes = optEu.compute()
RunKuRes = runKu.compute()
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
for i in EulRes:
    x1.append(i[0])
    y1.append(i[1])

for i in OptEuRes:
    x2.append(i[0])
    y2.append(i[1])
for i in RunKuRes:
    x3.append(i[0])
    y3.append(i[1])


plt.scatter(x1,y1,color = 'blue', label = 'Euler')
plt.scatter(x2,y2,color = 'red', label = 'OptEuler')
plt.scatter(x3,y3,color = 'green', label = 'Rung Kutta')
plt.legend(loc = 'best')
plt.show()