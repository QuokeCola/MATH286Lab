from __future__ import division
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
import time
sys.setrecursionlimit(100000)

start_Point = (0, 1)
Step = 0.001
HigherScale = 0.43
LowerScale = -5

Prob1AnalyticalEnable = False
GraphicEnable = True

Analytical_Subjects = 1000
Analytical_Points = 100
enable_safe_print = False


def diffF(x,y):
    return y*y*y+x*y*y+x*x*y+x*x*x

def Single_Calculation(Step, end_Scale):

    euler = Euler(diffF, Step, start_Point, end_Scale)
    optEu = OptEu(diffF, Step, start_Point, end_Scale)
    runKu = RunKu(diffF, Step, start_Point, end_Scale)
    start_time = time.time()
    EulRes = euler.compute()
    end_time = time.time()
    print("[\033[1;33mInfo\033[0m] Euler Algorithm Spent Time:" + str(end_time - start_time) + 'seconds')
    start_time = time.time()
    OptEuRes = optEu.compute()
    end_time = time.time()
    print("[\033[1;33mInfo\033[0m] Improved Euler Algorithm Spent Time:" + str(end_time - start_time) + 'seconds')
    start_time = time.time()
    RunKuRes = runKu.compute()
    end_time = time.time()
    print("[\033[1;33mInfo\033[0m] Runge Kutta Algorithm Spent Time:" + str(end_time - start_time) + 'seconds')
    return (RunKuRes, RunKuRes, RunKuRes, end_Scale)

def showRes(ResTup):
    print('-----------------Trial '+str(ResTup[3]) +'-----------------')
    if not (str(ResTup[0][1][-1]).find('inf') == -1) and enable_safe_print:
        print('[\033[1;31mWarning\033[0m] Euler Overflow')
    else:
        print('Euler: ' + str(ResTup[0][1][-1]))

    if not (str(ResTup[1][1][-1]).find('inf') == -1) and enable_safe_print:
        print('[\033[1;31mWarning\033[0m] Advanced Euler Overflow')
    else:
        print('Opt Euler: ' + str(ResTup[1][1][-1]))
    if not (str(ResTup[2][1][-1]).find('inf') == -1) and enable_safe_print:
        print('[\033[1;31mWarning\033[0m] Rung Kutta Overflow')
    else:
        print('Rung Kutta: ' + str(ResTup[2][1][-1]))

def log_Res(Res):
    file = open('result.csv','w')
    header = 'x,Euler, Advanced Euler, Rung Kutta\n'
    lines = [header]
    for i in range(len(Res[0][0])):
        lines.append(str(Res[2][0][i])+','+ str(Res[0][1][i])+ ',' + str(Res[1][1][i])+ ','+str(Res[2][1][i])+ '\n')
    file.writelines(lines)
    file.close()

if __name__ == '__main__':

    # Run Calculation
    print("[\033[1;33mInfo\033[0m] Start Computing Numerical Results")
    PosRes=Single_Calculation(Step, HigherScale)
    NegRes=Single_Calculation(-Step, LowerScale)
    Res = [[np.hstack((NegRes[0][0][::-1], PosRes[0][0])), np.hstack((NegRes[0][1][::-1], PosRes[0][1]))],
           [np.hstack((NegRes[1][0][::-1], PosRes[1][0])), np.hstack((NegRes[1][1][::-1], PosRes[1][1]))],
           [np.hstack((NegRes[2][0][::-1], PosRes[2][0])), np.hstack((NegRes[2][1][::-1], PosRes[2][1]))]]

    print("[\033[1;32mInfo\033[0m] Numerical Compute Finished")
    showRes(PosRes)
    print('[\033[1;33mInfo\033[0m] Start log Results')
    log_Res(PosRes)
    print('[\033[1;32mInfo\033[0m] Log Results Finished')

    # Run Analytical Results
    if (Prob1AnalyticalEnable):
        analy = analytical()
        analy.generate_subs(Analytical_Subjects)
        anares = analy.compute(HigherScale, Analytical_Points)

    # Plot Direction Field
    LowX = NegRes[0][0][-1]
    HighX = PosRes[0][0][-1]
    LowY = NegRes[2][1][-1]
    HighY = start_Point[1]
    for i in range(len(PosRes[2][1])):

        if not str(PosRes[2][1][i]).find('inf') == -1:
            HighY = PosRes[2][1][i - 1]
            print(HighY)
            break
    if Prob1AnalyticalEnable:
        for i in range(len(anares[1])):
            if not str(anares[1][i]).find('inf') == -1:
                HighY = anares[1][i-1]
                print(HighY)
                break
        if HighY == start_Point[1]:
            HighY = anares[1][-1]
    HighY = PosRes[2][1][-1]
    if GraphicEnable:
        funcDF = FunDF(diffF,LowX,HighX,0,HighY,20,20)
        funcDF.generate()

        # Plot Points
        print("[\033[1;33mInfo\033[0m] Add points to plot")
        plt.plot(Res[0][0], Res[0][1], '-', color ='blue', label ='Euler')
        plt.plot(Res[1][0], Res[1][1], '-', color ='red', label ='OptEuler')
        plt.plot(Res[2][0], Res[2][1], '-', color ='green', label ='Rung Kutta')
        if Prob1AnalyticalEnable:
            plt.plot(anares[0], anares[1], color = 'purple', label ='Analysis')
        plt.legend(loc = 'best')
        print("[\033[1;32mInfo\033[0m] Points added to plot")
        print("[\033[1;33mInfo\033[0m] Generating plot")
        plt.show()
        print("[\033[1;32mInfo\033[0m] Plot Generated")