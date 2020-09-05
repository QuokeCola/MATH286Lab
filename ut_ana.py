from analytical import *
import numpy as np
if __name__ == '__main__':
    analy = analytical()
    analy.generate_subs(1000)
    AnaRes = analy.compute(0.8,2)
    print(AnaRes[0][-1])
    print(AnaRes[1][-1])