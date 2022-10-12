def display(list1 , list2):
    """A function that prints the expression and displays the final result.

        Parameters: list1: List of Values
                    list2: List of Operators
                    finalExpression: The expression with 3 values and 2 operators
        Return: None

        """
    print(list1[0], list2[0], list1[1], list2[1], list1[2], list2[2], list1[3])

display([5,55,555,830],['*','+','='])