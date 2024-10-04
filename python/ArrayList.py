class ArrayList:
    def __init__(self) -> None:
        pass;

    def DisplayFirstAndLastElement(self, arrVar):
        first = arrVar[0];
        last = arrVar[-1];
        print("First Element: %s, Second Element: %s" % (first, last));