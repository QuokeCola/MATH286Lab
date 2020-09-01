from Euler_Method import *
def diffF(x,y):
    return y**2+x*y+x**2
obj1 = Euler(diffF,-0.01,(1,0),-5)
res = obj1.compute()
print(res)