class StringManipulation:
    def __init__(self) -> None:
        pass;

    def generatTuplesAndList(self, data):
        list = data.split(",");
        tup = tuple(list);

        print("List: ", list);
        print("Tuple: ", tup);

    def multiLineString(self):
        print("""
            a string that you "don't" have to escape                                                                      
            This                                                                                                          
            is a  ....... multi-line                                                                                      
            heredoc string --------> example 
        """)