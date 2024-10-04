class SwapString:
    def __init__(self) -> None:
        pass;
    def swap(self, firstString, secondString):
        tmp = firstString;
        firstString = secondString;
        secondString = tmp;
        print("First String: %s, Second String: %s" % (firstString, secondString));