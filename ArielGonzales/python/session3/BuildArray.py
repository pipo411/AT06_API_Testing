# Function 1
#  No arguments defined
# Should ask to the user the number of elements in the list
# According the value inserted ask for each value of the array and push it in a new array
# Return the array

list = []


def function1():
    global list
    tam_lista = int(input("Put the length  for the array :"))
    for i in range(tam_lista):
        print("Put your value in the position", i)
        value = input()
        list.append(value)
    return list


def function2():
    return list


print("Your array added is: ", function1())
print("Your array added is from function 1 is : ", function2())
