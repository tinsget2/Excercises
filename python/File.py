class File:
    def __init__(self) -> None:
        pass;
    def fileExtention(self, name):
        f_extention = name.split(".");
        print("The file extention is: ", f_extention[-1]);