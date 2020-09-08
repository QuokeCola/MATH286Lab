import numpy as np
import multiprocessing
from processbar import *
class analytical:
    def __init__(self):

        self.a = [0,0,0,0]
        self.a[0] = 1.0
        self.a[1] = self.a[0] ** 2
        self.a[2] = 0.5 * (2 * self.a[0] * self.a[1] + self.a[0])
        self.a[3] = (1 + self.a[1] ** 2 + 2 * self.a[0] * self.a[2] + self.a[1])/3
        self.y_list = []
        self.point_nums = 1

    def generate_subs(self, subs):
        print("[\033[1;33mInfo\033[0m] Start Computing Analytical Subjects")
        while len(self.a) < subs:
            new_a = self.a[len(self.a)-2]
            for i in range(0, len(self.a)):
                new_a += self.a[i]*self.a[len(self.a)-1-i]
            self.a.append(new_a/len(self.a))

            if len(self.a)%100 == 0:
                Percent = len(self.a)/subs
                end_str = '100%'
                process_bar(Percent, end_str=end_str, total_length=15)

        print("\n[\033[1;32mInfo\033[0m] Successfully Compute Analytical Subjects")

    def callbackfunc(self, retval):
        self.y_list.append(retval)
        Percent = len(self.y_list) / self.point_nums
        end_str = '100%'
        process_bar(Percent, end_str=end_str, total_length=15)

    def single_step(self, x):
        y = 0
        y+=self.a[0]
        for i in range(1, len(self.a)):
            y += self.a[i] * (x ** i)
        return y

    def compute(self, end_scale, point_nums = 1):
        print("[\033[1;33mInfo\033[0m] Start Compute Analytical Result")
        pool = multiprocessing.Pool()
        x_list = np.linspace(0, end_scale, point_nums)
        self.point_nums = point_nums

        for item in x_list:
            pool.apply_async(self.single_step,[item],callback=self.callbackfunc)
        pool.close()
        pool.join()
        print("\n[\033[1;32mInfo\033[0m] Successfully Compute Analytical Result")
        return (x_list, self.y_list)
