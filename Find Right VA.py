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
Step = 0.0001
sys.setrecursionlimit(100000)

def diffF(x,y):
    return y*y+x*y+x*x

def Single_Calculation(end_Scale):
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

def process_bar(percent, start_str='', end_str='', total_length=0):
    bar = ''.join(["\033[47m%s\033[0m"%'   '] * int(percent * total_length)) + ''
    bar = '\r' + start_str + bar.ljust(total_length) + ' {:0>4.1f}%|'.format(percent*100) + end_str
    print(bar, end='', flush=True)

def callbackfunc(retval):
    FinalRes.append(retval)
    percent = len(FinalRes) / len(end_Scale_D)
    end_str = '100%'
    process_bar(percent, start_str='', end_str=end_str, total_length=15)

if __name__ == '__main__':
    # Initialize
    pool = multiprocessing.Pool()
    end_Scale_D = np.linspace(0.85,0.86,100)
    FinalRes = []

    # Run Calculation
    print("[\033[1;33mInfo\033[0m] Start Computing Numerical Results")
    for item in end_Scale_D:
        pool.apply_async(Single_Calculation, args=[item], callback=callbackfunc)
    pool.close()
    pool.join()
    for res in FinalRes:
        showRes(res)
    print("[\033[1;32mInfo\033[0m] Numerical Compute Finished")

    # Run Analytical Results

    analy = analytical()
    analy.generate_subs(200)
    AnaRes = analy.compute(0.85, 10000)

    # Plot Direction Field
    funcDF = FunDF(diffF,-5,5,-5,10000,100,100)
    funcDF.generate()

    # Plot Points
    plt.scatter(FinalRes[0][0][0][0],FinalRes[0][0][0][1],color = 'blue', label = 'Euler')
    plt.scatter(FinalRes[0][1][0][0],FinalRes[0][1][0][1],color = 'red', label = 'OptEuler')
    plt.scatter(FinalRes[0][2][0][0],FinalRes[0][2][0][1],color = 'green', label = 'Rung Kutta')
    plt.scatter(AnaRes[0], AnaRes[1], color ='purple', label ='Analysis')
    plt.legend(loc = 'best')
    plt.show()
    print("[\033[1;32mInfo\033[0m] Plot Generated")