class Calculator:
    def __init__(self) -> None:
        pass

    def addition(num1):
        print("Enter aditional number: ", num1, " + ");
        num2 = float(input());
        sum = num1 + num2;
        return sum;

    def subtraction(num1):
        print("Enter aditional number: ", num1, " - ");
        num2 = float(input());
        sub = num1 - num2;
        return sub;

    def multiplication(num1):
        print("Enter aditional number: ", num1, " * ");
        num2 = float(input());
        mul = num1 * num2;
        return mul;

    def division(num1):
        print("Enter aditional number: ", num1, " / ");
        num2 = float(input());
        div = num1 + num2;
        return div;


    def calculate(self):
        print("Enter number");
        num1 = float(input());
        itr = 1;      

        while(itr):            
            print("Enter operator: ", num1);
            opr = input();

            if(opr == '+'):                
                num1 = Calculator.addition(num1);
            elif(opr == '-'):
                num1 = Calculator.subtraction(num1);
            elif(opr == '*'):
                num1 = Calculator.multiplication(num1);
            elif(opr == '/'):
                num1 = Calculator.division(num1);
            print("Do you want to continue (1/0)");
            itr = int(input());

        print("Result: ", num1);
    

