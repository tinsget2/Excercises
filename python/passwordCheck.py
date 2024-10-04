import re


class PasswordCheck:
    def __init__(self):
        pass

    def inputpassword(self):
        testPass = input("Input your password ")
        return self.passwordCheck(testPass)

    def passwordCheck(self, testPass):
        test = ''

        if 6 > len(testPass) > 16:
            test = """     number               
    At least 1 letter between [a-z] and 1 letter between [A-Z].
    At least 1 number between [0-9].
    At least 1 character from [$#@].
    Minimum length 6 characters.
    Maximum length 16 characters.
                    """
        elif not re.search("[a-z]", testPass):
            test = """     letter               
    At least 1 letter between [a-z] and 1 letter between [A-Z].
    At least 1 number between [0-9].
    At least 1 character from [$#@].
    Minimum length 6 characters.
    Maximum length 16 characters.
                    """
        elif not re.search("[A-Z]", testPass):
            test = """        A-Z            
    At least 1 letter between [a-z] and 1 letter between [A-Z].
    At least 1 number between [0-9].
    At least 1 character from [$#@].
    Minimum length 6 characters.
    Maximum length 16 characters.
                    """
        elif not re.search("[1-9]", testPass):
            test = """        1-9            
    At least 1 letter between [a-z] and 1 letter between [A-Z].
    At least 1 number between [0-9].
    At least 1 character from [$#@].
    Minimum length 6 characters.
    Maximum length 16 characters.
                    """
        elif not re.search("[@#$]", testPass):
            test = """                 @   
    At least 1 letter between [a-z] and 1 letter between [A-Z].
    At least 1 number between [0-9].
    At least 1 character from [$#@].
    Minimum length 6 characters.
    Maximum length 16 characters.
                    """
        elif re.search("\s", testPass):
            test = """         space           
    At least 1 letter between [a-z] and 1 letter between [A-Z].
    At least 1 number between [0-9].
    At least 1 character from [$#@].
    Minimum length 6 characters.
    Maximum length 16 characters.
                    """
        else:
            test = "Password is in the correct format"

        return test


p = PasswordCheck()
print(p.inputpassword())
