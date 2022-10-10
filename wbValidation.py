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

def main():
    i=0
    while i==0:
        inttest=int(input("input integer to test  "))
        val2=valInteger(inttest)
        operatorTest=input("enter operator to test  ")
        val1=valOperator(operatorTest)
        print(val1, val2)
        i=int(input("press 1 to exit or 0 to continue "))

if __name__ == '__main__':
    main()