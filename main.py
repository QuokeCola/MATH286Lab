from Euler_Method import *
from Opt_Euler_Method import *
from RungKutta_Method import *
from analytical import *
import math

import matplotlib.pyplot as plt
import numpy as np

def diffF(x,y):
    return y**2+x*y+x**2

start_Point = (0,1)
end_Scale = 0.9
Step = 0.001

euler = Euler(diffF, Step, start_Point, end_Scale)
optEu = OptEu(diffF, Step, start_Point, end_Scale)
runKu = RunKu(diffF, Step, start_Point, end_Scale)
analy = analytical(800)
EulRes = euler.compute()
OptEuRes = optEu.compute()
RunKuRes = runKu.compute()
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
for i in EulRes:
    x1.append(i[0])
    y1.append(i[1])

for i in OptEuRes:
    x2.append(i[0])
    y2.append(i[1])
for i in RunKuRes:
    x3.append(i[0])
    y3.append(i[1])

x,y = np.meshgrid(np.linspace(-5,5,20),np.linspace(-5,5,20))
u = np.linspace(1,1,400)
u = u.reshape(20,20)
v = np.linspace(0,0,400)
v = v.reshape(20,20)
for i in range(0,20):
    for j in range(0,20):
        v[i][j] = (diffF(x[i][j],y[i][j]))/math.sqrt(1+diffF(x[i][j],y[i][j])*diffF(x[i][j],y[i][j]))
        u[i][j] = 1/math.sqrt(1+diffF(x[i][j],y[i][j])*diffF(x[i][j],y[i][j]))

plt.quiver(x,y,u,v)

plt.scatter(x1,y1,color = 'blue', label = 'Euler')
plt.scatter(x2,y2,color = 'red', label = 'OptEuler')
plt.scatter(x3,y3,color = 'green', label = 'Rung Kutta')
plt.scatter(x4,AnaRes, color = 'purple', label = 'Analysis')
plt.legend(loc = 'best')
plt.show()

print(EulRes[-1])