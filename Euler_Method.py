import numpy as np
class Euler(object):
    point_hist = []
    res = ([],False)
    def __init__(self, diff_func, step, start_point, stop_range):
        self.diff_func = diff_func
        self.step = step
        self.start_point = start_point
        self.stop_range = stop_range
        self.overFlow = False
        self.x = np.arange(start_point[0],stop_range,step)
        self.y = [start_point[1]]

    def compute(self):
        for i in self.x:
            f = self.diff_func(i,self.y[len(self.y)-1])
            y_new = self.y[len(self.y)-1]+self.step*f
            self.y.append(y_new)
        self.y.pop()
        return ([self.x, self.y], False)

