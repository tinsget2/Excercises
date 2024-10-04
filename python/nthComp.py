class nthComp:
    def __init__(self) -> None:
        pass

    def nthComp(self, n):
        n1 = int("%s" % n)
        n2 = int("%s%s" % (n,n))
        n3 = int("%s%s%s" % (n, n, n))
        nsum = n1 + n2 + n3
        print(nsum)


nn = nthComp()
nn.nthComp(5)
