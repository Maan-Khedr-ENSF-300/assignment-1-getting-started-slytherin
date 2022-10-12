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
    print("CODE WORKS!!!!!!!!!")

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
