class Between1500to2700:
    def __init__(self):
        pass

    def between1500to2700(self):
        str1 = []
        for n in range(1500, 2701):
            if n % 5 == 0 and n % 7 == 0:
                str1.append(str(n))
        return (", ".join(str1))


b = Between1500to2700()
print(b.between1500to2700())