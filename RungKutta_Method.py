import numpy as np
from processbar import *
class RunKu(object):
    point_hist = []

    def __init__(self, diff_func, step, start_point, stop_range):
        self.diff_func = diff_func
        self.step = step
        self.start_point = start_point
        self.stop_range = stop_range
        self.overFlow = False
        self.x = np.arange(start_point[0],stop_range,step)
        self.y = [start_point[1]]

    def compute(self):
        print("[\033[1;33mInfo\033[0m] Start Computing Runge Kutta Results")
        end_Str = '100%'
        count = 0
        for i in self.x:
            count += 1
            percent = len(self.y) / len(self.x)
            if count % int(len(self.x) / 100) == 0:
                process_bar(percent=percent, end_str=end_Str)
            try:
                k1 = self.diff_func(i, self.y[len(self.y)-1])
                x_1 = i + self.step * 0.5
                y_1 = self.y[len(self.y)-1] + self.step * k1 * 0.5
                k2 = self.diff_func(x_1, y_1)
                x_2 = i + self.step * 0.5
                y_2 = self.y[len(self.y)-1] + self.step * k2 * 0.5
                k3 = self.diff_func(x_2, y_2)
                x_3 = i + self.step
                y_3 = self.y[len(self.y)-1] + self.step * k3
                k4 = self.diff_func(x_3, y_3)
                y_new = self.y[len(self.y)-1] + self.step / 6 * (k1 + 2 * (k2 + k3) + k4)
                self.y.append(y_new)
            except OverflowError:
                return ([self.x, self.y], True)
        self.y.pop()
        print("\n[\033[1;32mInfo\033[0m] Compute Runge Kutta Results Finished")
        return ([self.x, self.y], False)