# Comparation of two arguments equals.
def arithmetic_equal(text1, text2):
    if (len(text1) == len(text2)):
        return ("They are Equals")


# Comparation of two arguments different.
def arithmetic_notEqual(num1, num2):
    if (num1 != num2):
        return ("They are not equal ")


# Comparation of two arguments greater operation.
def arithmetic_greater(num1, num2):
    if (num1 > num2):
        return (num1, "is greater than", num2)
    else:
        return (num2, "is greater than", num1)


# Comparation of two arguments less operation.
def arithmetic_less(num1, num2):
    if (num1 < num2):
        return (num1, "is less than", num2)
    else:
        return (num2, "is less than", num1)


# Comparation of two arguments greater or equal operation.
def arithmetic_greaterEqual(num1, num2):
    if (num1 >= num2):
        return (num1, "is greater or equal than", num2)
    else:
        return (num2, "is greater or equal than", num1)


# Comparation of two arguments less or equal operation.
def arithmetic_lessEqual(text1, text2):
    if (len(text1) <= len(text2)):
        return (text1, "is less or equal characters than", text2)
    else:
        return (text2, "is less or equal characters than", text1)


# Equal operation
print(arithmetic_equal("oranges", "oranges"))
# Not equal operation
print(arithmetic_notEqual(7, 5))
# Greater operation
print("Greater operation", arithmetic_greater(5, 20))
# Less operation
print("Less operation", arithmetic_less(-9, -21))
# Greater or Equal operation
print("Greater or Equal operation", arithmetic_greaterEqual(8, -15))
# Less or Equal operation
print("Less or Equal operation", arithmetic_lessEqual("orange", "raspberry"))
