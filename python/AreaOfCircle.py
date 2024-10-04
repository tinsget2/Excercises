class AreaOfCircle:
    PI = 3.14159

    def __init__(self) -> None:
        pass

    def area(self, rad):
        area = AreaOfCircle.PI * pow(rad, 2);
        print(area);

    def perimeter(self, rad):
        para = 2 * AreaOfCircle.PI * rad;
        print(para);
