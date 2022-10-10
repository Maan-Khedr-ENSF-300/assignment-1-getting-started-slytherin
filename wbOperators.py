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
def main():
    i=0
    while i==0:
        value_1 =int(input("input integer to test  "))
        value_2= int(input("input integer to test  ")) 
        print (myAdd(value_1, value_2))
        print (myDiv(value_1, value_2))
        print (myMul(value_1, value_2))
        print(mySub(value_1, value_2))
        i=int(input("press 1 to exit or 0 to continue "))
        

if __name__ == '__main__':
    main()