from __future__ import division
import multiprocessing
import sys

import warnings
warnings.filterwarnings("ignore")

from Euler_Method import *
from Opt_Euler_Method import *
from RungKutta_Method import *
from analytical import *
from Function_DF import *

import matplotlib.pyplot as plt
import numpy as np
sys.setrecursionlimit(100000)

start_Point = (0, 1)
Step = 0.01
EndScale = 0.85

Analytical_Subjects = 1000
Analytical_Points = 100


def diffF(x,y):
    return y*y+x*y+x*x

def Single_Calculation(Step, end_Scale):
    euler = Euler(diffF, Step, start_Point, end_Scale)
    optEu = OptEu(diffF, Step, start_Point, end_Scale)
    runKu = RunKu(diffF, Step, start_Point, end_Scale)
    EulRes = euler.compute()
    OptEuRes = optEu.compute()
    RunKuRes = runKu.compute()
    return (EulRes, OptEuRes, RunKuRes, end_Scale)

def showRes(ResTup):
    print('-----------------Trial '+str(ResTup[3]) +'-----------------')
    if not (str(ResTup[0][0][1][-1]).find('inf') == -1):
        print('[\033[1;31mWarning\033[0m] Euler Overflow')
    else:
        print('Euler: ' + str(ResTup[0][0][1][-1]))

    if not (str(ResTup[1][0][1][-1]).find('inf') == -1):
        print('[\033[1;31mWarning\033[0m] Advanced Euler Overflow')
    else:
        print('Opt Euler: ' + str(ResTup[1][0][1][-1]))
    if not (str(ResTup[2][0][1][-1]).find('inf') == -1):
        print('[\033[1;31mWarning\033[0m] Rung Kutta Overflow')
    else:
        print('Rung Kutta: ' + str(ResTup[2][0][1][-1]))

def log_Res(Res):
    file = open('result.csv','w')
    header = 'x,Euler, Advanced Euler, Rung Kutta\n'
    lines = [header]
    for i in range(len(Res[0][0][0])):
        lines.append(str(Res[2][0][0][i])+','+ str(Res[0][0][1][i])+ ',' + str(Res[1][0][1][i])+ ','+str(Res[2][0][1][i])+ '\n')
    file.writelines(lines)
    file.close()

if __name__ == '__main__':
    # Initialize
    pool = multiprocessing.Pool()
    end_Scale_D = np.linspace(0.85,0.86,100)
    FinalRes = []

    # Run Calculation
    print("[\033[1;33mInfo\033[0m] Start Computing Numerical Results")
    Res=Single_Calculation(Step,EndScale)
    print("[\033[1;32mInfo\033[0m] Numerical Compute Finished")
    print('[\033[1;33mInfo\033[0m] Start log Results')
    log_Res(Res)
    print('[\033[1;32mInfo\033[0m] Log Results Finished')

    # Run Analytical Results
    analy = analytical()
    analy.generate_subs(Analytical_Subjects)
    anares = analy.compute(EndScale, Analytical_Points)

    # Plot Direction Field
    LowX = Res[0][0][0][0]
    HighX = Res[0][0][0][-1]
    LowY = Res[2][0][1][0]
    HighY = start_Point[1]
    for i in range(len(Res[2][0][1])):

        if not str(Res[2][0][1][i]).find('inf') == -1:
            HighY = Res[2][0][1][i-1]
            print(HighY)
            break
    for i in range(len(anares[1])):
        if not str(anares[1][i]).find('inf') == -1:
            HighY = anares[1][i-1]
            print(HighY)
            break
    if HighY == start_Point[1]:
        HighY = anares[1][-1]
    funcDF = FunDF(diffF,LowX,HighX,LowY,HighY,20,20)
    funcDF.generate()

    # Plot Points
    print("[\033[1;33mInfo\033[0m] Add points to plot")
    plt.scatter(Res[0][0][0],Res[0][0][1],color = 'blue', label = 'Euler')
    plt.scatter(Res[1][0][0],Res[1][0][1],color = 'red', label = 'OptEuler')
    plt.scatter(Res[2][0][0],Res[2][0][1],color = 'green', label = 'Rung Kutta')
    plt.scatter(anares[0], anares[1], color ='purple', label ='Analysis')
    plt.legend(loc = 'best')
    print("[\033[1;32mInfo\033[0m] Points added to plot")
    print("[\033[1;33mInfo\033[0m] Generating plot")
    plt.show()
    print("[\033[1;32mInfo\033[0m] Plot Generated")