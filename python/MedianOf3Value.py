class MedianOf3Value:
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def Median(self):
        ls = [self.m1, self.m2, self.m3]
        prev = 0
        for n in range(3):
            if n == 0:
                prev = ls[0]
            else:
                if prev > ls[n]:
                    ls[n-1] = ls[n]
                    ls[n] = prev
                else:
                    prev = ls[n]
        med = int(3/2)

        print(ls[med])


m = MedianOf3Value(15, 26, 29)
m.Median()
