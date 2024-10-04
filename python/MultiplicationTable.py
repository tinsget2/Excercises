class MultiplicationTable:
    def __init__(self) -> None:
        pass
    def multiplication(self, num):
        for x in range(1,13):
            print("%d * %d = %d" % (num, x, num*x));
        