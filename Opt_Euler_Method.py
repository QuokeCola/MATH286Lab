class OptEu(object):
    point_hist = []

    def __init__(self, diff_func, step, start_point, stop_range):
        self.diff_func = diff_func
        self.step = step
        self.start_point = start_point
        self.stop_range = stop_range
        self.overFlow = False

    def compute(self):
        return self.loop(self.start_point)

    def h_S(self, num):
        print(num[0])
        print(num[1])
        print(self.start_point)

    def loop(self, point):
        x = point[0]
        y = point[1]
        outOfBounds = (x>self.stop_range and self.step > 0) or (x<self.stop_range and self.step < 0)
        if not outOfBounds:
            try:
                f_low = self.diff_func(x, y)
                x_high = x + self.step
                y_high = y + self.step * f_low
                f_high = self.diff_func(x_high, y_high)
                x_new = x_high
                y_new = y + self.step * 0.5 * (f_low + f_high)
                point_new = (x_new, y_new)
                self.point_hist.append(point_new)
                self.loop(point_new)
            except OverflowError:
                print('Warning: Optimize Euler Overflow')
                self.overFlow = True
                return (self.point_hist, self.overFlow)
        else:
            return (self.point_hist, self.overFlow)
        return (self.point_hist, self.overFlow)
