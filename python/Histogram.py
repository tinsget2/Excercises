class Histogram:
    def __init__(self):
        pass

    def histogram(self, lt):
        for n in lt:
            his = ''
            while n > 0:
                his = his + '*'
                n = n-1
            print(his)


h = Histogram()
h.histogram([2, 3, 6, 5])
