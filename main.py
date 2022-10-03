def operatorCall(num1,num2,operator):
    if(operator=='/'):
        eval=MyDiv(num1,num2)
    elif(operator=='*'):
        eval=(num1,num2)
    elif(operator=='+'):
        eval=myAdd(num1,num2)
    elif(operator=='-'):
        eval=mySub(num1,num2)
    return(eval)


def eval(numbersList, operatorsList):
    eval1=0
    finalSol=0
    if((operatorsList[1] == '/'or operatorsList[1] =='*') and (operatorsList[0]=="+" or operatorsList[0]=='-')):
        eval1 = operatorCall(numbersList[1],numbersList[2],operatorsList[2])
        finalSol=operatorCall(numbersList[0],eval1,operatorsList[1])
    else:
        eval1 = operatorCall(numbersList[1],numbersList[2],operatorsList[2])
        finalSol=operatorCall(numbersList[0],eval1,operatorsList[1])
    numbersList.append(finalSol)
    operatorsList.append("=")
    display(numbersList,operatorsList)

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

        

