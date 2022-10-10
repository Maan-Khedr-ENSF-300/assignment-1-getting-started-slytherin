
def operatorCall(num1,num2,operator):
    if(operator=='/'):
        eval=myDiv(num1,num2)
    elif(operator=='*'):
        eval=myMul(num1,num2)
    elif(operator=='+'):
        eval=myAdd(num1,num2)
    elif(operator=='-'):
        eval=mySub(num1,num2)
        
    return(eval)


def eval(numbersList, operatorsList):
    eval1=0
    finalSol=0
    if((operatorsList[0]=='/' and numbersList[1]==0)or (operatorsList[1]=='/' and numbersList[2]==0)):
        print("Cant divide by 0 :(")
        return 0
    elif((operatorsList[1] == '/'or operatorsList[1] =='*') and (operatorsList[0]=="+" or operatorsList[0]=='-')):
        eval1 = operatorCall(numbersList[1],numbersList[2],operatorsList[1])
        finalSol=operatorCall(numbersList[0],eval1,operatorsList[0])
    else:
        eval1 = operatorCall(numbersList[0],numbersList[1],operatorsList[0])
        finalSol=operatorCall(eval1,numbersList[2],operatorsList[1])
    numbersList.append(finalSol)
    operatorsList.append("=")
    display(numbersList,operatorsList)

def main():
    i=0
    while(i==0):
        firstValue = (input("Enter your first value: "))  
        firstOperator = input("Enter your first operator: ")
        secondValue = (input("Enter your second value: "))
        secondOperator = input("Enter your second operator: ")
        thirdValue = (input("Enter your third value: "))
        if( valOperator((firstOperator))==0 or valOperator(secondOperator)==0 or valInteger(int(firstValue))==0 or valInteger(int(secondValue))==0 or valInteger(int(thirdValue))==0 ):
            i=0
            print("One of the values were entered incorrectly")
        else:
            i=1
        listNumbers=[int(firstValue),int(secondValue),int(thirdValue)]
        listOperators=[firstOperator,secondOperator]
        eval(listNumbers,listOperators)
   
def display(list1 , list2):
    """A function that prints the expression and displays the final result.

        Parameters: list1: List of Values
                    list2: List of Operators
                    finalExpression: The expression with 3 values and 2 operators
        Return: None

        """
    print(list1[0], list2[0], list1[1], list2[1], list1[2], list2[2], list1[3])

        

def mySub( user_1,user_2): 
    """user defined function return the result of subtraction of two integers
    parameters : two 
    returns integer value
    """
    user_3 = user_1 - user_2
    return (user_3)

def myDiv( user_1,user_2): 
     """user defined function return the result of division of two integers
    parameters : two 
    returns integer value
    """
     user_3 = user_1 // user_2
     return (user_3)

def myAdd( user_1,user_2):
    """user defined function return the result of addition of two integers
    parameters : two 
    returns integer value
    """
    user_3 = user_1 + user_2
    return (user_3)
def myMul( user_1,user_2):
     """user defined function return the result of multiplication of two integers
    parameters : two 
    returns integer value
    """
     user_3 = user_1 * user_2
     return (user_3)

def valInteger (user_1):
    if(type(user_1)== int):
        return 1
    else: 
        return 0

def valOperator(user_1):
    if (user_1 == '/' or user_1 =="*" or user_1 == "+" or user_1 == "-"):
        return 1 
    else:
        return 0 


if __name__ == '__main__':
    main()


