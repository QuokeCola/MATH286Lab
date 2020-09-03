import numpy as np
class OptEu(object):
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
        for i in self.x:
            try:
                f_low = self.diff_func(i, self.y[len(self.y)-1])
                x_high = i + self.step
                y_high = self.y[len(self.y)-1] + self.step * f_low
                f_high = self.diff_func(x_high, y_high)
                y_new = self.y[len(self.y)-1] + self.step * 0.5 * (f_low + f_high)
                self.y.append(y_new)
            except OverflowError:
                return ([self.x, self.y], True)
        self.y.pop()
        return ([self.x, self.y], False)
