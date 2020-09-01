class analytical:
    def __init__(self, subs):
        self.subs = subs
        self.a = [0,0,0,0,0]
        self.a[0] = 1.0
        self.a[1] = self.a[0] ** 2
        self.a[2] = 0.5 * (2 * self.a[0] * self.a[1] + self.a[2])
        self.a[3] = (1 + self.a[1] ** 2 + 2 * self.a[0] * self.a[2] + self.a[1])
    def compute(self, x):
        #-------------------First Compute Subs-------------------
        while len(self.a) < self.subs:
            new_a = self.a[len(self.a)-2]
            for i in range(0, len(self.a)):
                new_a += self.a[i]*self.a[len(self.a)-1-i]
            self.a.append(new_a/len(self.a))
        y = 0
        for i in range(0,len(self.a)):
            y += self.a[i]*(x**i)
        return y