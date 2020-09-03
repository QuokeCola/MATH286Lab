from __future__ import division

import warnings
warnings.filterwarnings("ignore")

from Euler_Method import *
from Opt_Euler_Method import *
from RungKutta_Method import *
from analytical import *
from Function_DF import *

import multiprocessing

import sys

import matplotlib.pyplot as plt
import numpy as np

start_Point = (0, 1)
Default_Step = 0.01
sys.setrecursionlimit(100000)

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
    if (str(ResTup[0][0][1][-1]) == 'inf'):
        print('[\033[1;31mWarning\033[0m] Euler Overflow')
    else:
        print('Euler: ' + str(ResTup[0][0][1][-1]))

    if (str(ResTup[1][0][1][-1]) == 'inf'):
        print('[\033[1;31mWarning\033[0m] Advanced Euler Overflow')
    else:
        print('Opt Euler: ' + str(ResTup[1][0][1][-1]))
    if (str(ResTup[2][0][1][-1]) == 'inf'):
        print('[\033[1;31mWarning\033[0m] Rung Kutta Overflow')
    else:
        print('Rung Kutta: ' + str(ResTup[2][0][1][-1]))

if __name__ == '__main__':
    # Initialize
    pool = multiprocessing.Pool()
    end_Scale_D = np.linspace(0.85,0.86,100)
    FinalRes = []

    # Run Calculation
    print("[\033[1;33mInfo\033[0m] Start Computing Numerical Results")
    y = start_Point[1]
    x = start_Point[0]+Default_Step * 10
    Step = Default_Step
    trial = 0
    # while Step > 0.001:
    #     print('[\033[1;32mInfo\033[0m]Running Trial' + str(trial))
    #     y = 0
    #     while not (str(y) == 'inf' or str(y) == '-inf'):
    #         x += Step
    #         Res = Single_Calculation(0.001, x)
    #         y = Res[2][0][1][-1]
    #         print('[\033[1;32mStatus\033[0m]On range ' + str(x))
    #     x = x - Step
    #     Step = Step / 2
    #     trial += 1
    # x -= (Step*2)
    # Res = Single_Calculation(Step, x)
    Res = Single_Calculation(0.000001, 0.858876)
    showRes(Res)
    # for i in np.linspace(0.8588867,0.828800,68):
    # for res in FinalRes:
    #     showRes(res)
    print("[\033[1;32mInfo\033[0m] Numerical Compute Finished")

    # Run Analytical Results

    # analy = analytical()
    # analy.generate_subs(2000)
    # AnaRes = analy.compute(0.88, 1000)
    # # for i in range(len(AnaRes[0])):
    # #     print(AnaRes[1][i])
    # #     if str(AnaRes[1][i]) == 'inf':
    # #         print(AnaRes[0][i-1])
    # #         break
    # # Plot Direction Field
    # funcDF = FunDF(diffF,-5,5,-5,10000,100,100)
    # funcDF.generate()
    #
    # # Plot Points
    # plt.scatter(Res[0][0][0],Res[0][0][1],color = 'blue', label = 'Euler')
    # plt.scatter(Res[1][0][0],Res[1][0][1],color = 'red', label = 'OptEuler')
    # plt.scatter(Res[2][0][0],Res[2][0][1],color = 'green', label = 'Rung Kutta')
    # plt.scatter(AnaRes[0], AnaRes[1], color ='purple', label ='Analysis')
    # plt.legend(loc = 'best')
    # plt.show()
    # print("[\033[1;32mInfo\033[0m] Plot Generated")