from analytical import *

if __name__ == '__main__':
    obj1 = analytical()
    obj1.generate_subs(4000)
    res = obj1.compute(0.8,2)
    print(res[1][-1])
