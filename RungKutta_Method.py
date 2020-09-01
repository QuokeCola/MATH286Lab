class RunKu(object):
    point_hist = []

    def __init__(self, diff_func, step, start_point, stop_range):
        self.diff_func = diff_func
        self.step = step
        self.start_point = start_point
        self.stop_range = stop_range

    def compute(self):
        return self.loop(self.start_point)

    def h_S(self, num):
        print(num[0])
        print(num[1])
        print(self.start_point)

    def loop(self, point):
        x = point[0]
        y = point[1]
        if x < self.stop_range:
            k1 = self.diff_func(x, y)
            x_1 = x + self.step * 0.5
            y_1 = y + self.step * k1 * 0.5
            k2 = self.diff_func(x_1, y_1)
            x_2 = x + self.step * 0.5
            y_2 = y + self.step * k2 * 0.5
            k3 = self.diff_func(x_2, y_2)
            x_3 = x + self.step
            y_3 = y + self.step * k3
            k4 = self.diff_func(x_3, y_3)
            x_new = x + self.step
            y_new = y + self.step/6 * (k1 + 2*(k2 + k3) + k4)
            point_new = (x_new, y_new)
            self.point_hist.append(point_new)
            self.loop(point_new)
        else:
            return self.point_hist
        return self.point_hist
