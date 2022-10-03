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
    user_3 = user_1 / user_2
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
    if(type(user_1)== "int"):
        return 1
    else: 
        return 0
def valOperator(user_1):
    if (user_1 == '/' or user_1 =="*" or user_1 == "+" or user_1 == "-"):
        return 1 
    else:
        return 0 

