class TriangleSide:
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def sizeCheck(self):
        if self.s1 == self.s2 and self.s1 == self.s3 and self.s2 == self.s3:
            return "Equilateral"
        elif self.s1 == self.s2 or self.s1 == self.s3 or self.s2 == self.s3:
            return "Isosceles"
        else:
            return "Scalene"


t = TriangleSide(6, 8, 12)
print(t.sizeCheck())