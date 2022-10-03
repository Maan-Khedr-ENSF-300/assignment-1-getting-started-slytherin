def main():
    i=0
    while(i==0):
        firstValue = input("Enter your first value: ")  
        firstOperator = input("Enter your first operator: ")
        secondValue = input("Enter your second value: ")
        secondOperator = input("Enter your second operator: ")
        thirdValue = input("Enter your third value: ")
        if( valOperator(firstOperator)==0 or valOperator(secondOperator)==0 or valInteger(firstValue)==0 or valInteger(secondValue)==0 or valInteger(thirdValue)==0 ):
            i=0
            print("One of the values were entered incorrectly")
        else:
            i=1
    
def display(list1 , list2):
    """A function that prints the expression and displays the final result.

        Parameters: list1: List of Values
                    list2: List of Operators
                    finalExpression: The expression with 3 values and 2 operators
        Return: None

        """
    print(list1[0], list2[0], list1[1], list2[1], list1[2], list2[2], list1[3])
