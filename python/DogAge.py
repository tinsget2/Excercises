class DogAge:
    #input should be number
    def __init__(self):
        pass

    def inputAge(self):
        age = input("Input dog age ")
        return self.dogAge(age)

    def dogAge(self, age):
        ageint = int(age)
        dogAge = 0
        for n in range(ageint):
            if n < 2:
                dogAge += 10.5
            else:
                dogAge += 4

        return dogAge


d = DogAge()
print(d.inputAge())
