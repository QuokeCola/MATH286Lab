import matplotlib.pyplot as plt
import numpy as np
import math
class FunDF:
    def __init__(self, func, low_x, high_x, low_y, high_y, x_res, y_res):
        self.func = func
        self.low_x = low_x
        self.low_y = low_y
        self.high_x = high_x
        self.high_y = high_y
        self.x_res = x_res
        self.y_res = y_res
        
    def generate(self):
        print("[\033[1;33mInfo\033[0m] Initializing Meshes")
        x, y = np.meshgrid(np.linspace(self.low_x, self.high_x, self.x_res), np.linspace(self.low_y, self.high_y, self.y_res))
        u = np.linspace(1, 1, self.x_res*self.y_res)
        u = u.reshape(self.x_res, self.y_res)
        v = np.linspace(0, 0, self.x_res*self.y_res)
        v = v.reshape(self.x_res, self.y_res)
        print("[\033[1;32mInfo\033[0m] Successfully initialize Meshes")
        print("[\033[1;33mInfo\033[0m] Initializing Direction Field")
        for i in range(0, self.x_res):
            for j in range(0, self.y_res):
                v[i][j] = (self.func(x[i][j], y[i][j])) / math.sqrt(1 + self.func(x[i][j], y[i][j]) * self.func(x[i][j], y[i][j])) * (self.high_x - self.low_x)/(self.high_y - self.low_y)
                u[i][j] = 1 / math.sqrt(1 + self.func(x[i][j], y[i][j]) * self.func(x[i][j], y[i][j]))
        #plt.figure(figsize=(108, 81), dpi=100.0)
        plt.quiver(x, y, u, v)
        print("[\033[1;32mInfo\033[0m] Successfully initialize Direction Field")