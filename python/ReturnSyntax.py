class ReturnSyntax:
    def __init__(self) -> None:
        pass

    def returnSyntax(self, func):
        print(func.__doc__)
        print(func.__name__)


rs = ReturnSyntax()
rs.returnSyntax(abs)