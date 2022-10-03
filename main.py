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
        

