#The function recieve three arguments operation and two numbers
def perform_operation(operator,num1,num2):
    if(operator == "+"):
        return (num1 + num2)
    if(operator == "-"):
        return (num1 - num2)
    if (operator == "*"):
        return (num1 * num2)
    if (operator == "/"):
        return (num1 / num2)
    if (operator == "%"):
        return (num1 % num2)
    if (operator == "//"):
        return (num1 // num2)

#Addition
print("The operator input is + the answer is",perform_operation("+",9,3))
#Substraction
print("The operator input is - the answer is",perform_operation("-",15,35))
#Multiplication
print("The operator input is * the answer is",perform_operation("*",8,9))
#Division
print("The operator input is / the answer is",perform_operation("/",85,8))
#Modulus
print("The operator input is % the answer is",perform_operation("%",15,3))
#Floor Division
print("The operator input is // the answer is",perform_operation("//",15,3))


