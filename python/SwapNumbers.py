class SwapNumbers:
    def __init__(self) -> None:
        pass;
    def swap(self, num1, num2):
        tmp = num1;
        num1 = num2;
        num2 = tmp;
        print("First number: %d, Second number: %d" % (num1, num2));