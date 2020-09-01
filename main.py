from Euler_Method import *
from Opt_Euler_Method import *
from RungKutta_Method import *
from analytical import *
import math

import sys
sys.setrecursionlimit(100000)

import matplotlib.pyplot as plt
import numpy as np

def diffF(x,y):
    return y**2+x*y+x**2

start_Point = (0,1)
end_Scale = 0.86
Step = 0.0001

for end_Scale in np.linspace(0.85,0.86,100):

    print('-----------------Trial '+str(end_Scale) +'-----------------')
    euler = Euler(diffF, Step, start_Point, end_Scale)
    optEu = OptEu(diffF, Step, start_Point, end_Scale)
    runKu = RunKu(diffF, Step, start_Point, end_Scale)
    EulRes = euler.compute()
    OptEuRes = optEu.compute()
    RunKuRes = runKu.compute()
    print(EulRes[1])
    if (EulRes[1] or OptEuRes[1]) or RunKuRes[1]:
        break
    print('Euler: ' + str(EulRes[0][-1]))
    print('Opt Euler:' + str(OptEuRes[0][-1]))
    print('Rung Kutta: ' + str(RunKuRes[0][-1]))
    print(' ')


analy = analytical(800)
AnaRes = []
x4 = []
for i in np.linspace(start_Point[0],end_Scale,100):
    AnaRes.append(analy.compute(i))
    x4.append(i)

x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
for i in EulRes[0]:
    x1.append(i[0])
    y1.append(i[1])

for i in OptEuRes[0]:
    x2.append(i[0])
    y2.append(i[1])

for i in RunKuRes[0]:
    x3.append(i[0])
    y3.append(i[1])
print("successfully Load Results")
x,y = np.meshgrid(np.linspace(-5,5,20),np.linspace(-5,5,20))
u = np.linspace(1,1,400)
u = u.reshape(20,20)
v = np.linspace(0,0,400)
v = v.reshape(20,20)

print("successfully initialize Meshes")
for i in range(0,20):
    for j in range(0,20):
        v[i][j] = (diffF(x[i][j],y[i][j]))/math.sqrt(1+diffF(x[i][j],y[i][j])*diffF(x[i][j],y[i][j]))
        u[i][j] = 1/math.sqrt(1+diffF(x[i][j],y[i][j])*diffF(x[i][j],y[i][j]))
print("successfully initialize Analytic Plot")
plt.quiver(x,y,u,v)
print("successfully initialize Direction Field")
plt.scatter(x1,y1,color = 'blue', label = 'Euler')
plt.scatter(x2,y2,color = 'red', label = 'OptEuler')
plt.scatter(x3,y3,color = 'green', label = 'Rung Kutta')
plt.scatter(x4,AnaRes, color = 'purple', label = 'Analysis')
plt.legend(loc = 'best')
plt.show()