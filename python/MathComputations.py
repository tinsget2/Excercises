import math


class MathComputations:
    def __init__(self):
        pass

    def volumeofsphere(self, radius):
        r = radius
        pi = math.pi
        v = (4 * pi * r ** 3) / 3

        print("Volume of sphere: ", v)


m = MathComputations()
m.volumeofsphere(6)
