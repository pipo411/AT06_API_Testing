import re

dictionary = {}


# Create a Dictionary.
def createDictionary():
    global dictionary
    while True:
        try:
            tam = int(input("Set the lenght of the dictionary: "))
            break
        except ValueError:
            print("Invalid Input")
    for i in range(tam):
        while True:
            try:
                key = int(input("Set the Key between 1 to 100: "))
                if not 0 < key < 101:
                    invalid_key = ValueError("{0} is not a valid key".format(key))
                    raise invalid_key
                values = input("Set the value: ")
                if not re.fullmatch("^[a-z]{1,8}", values):
                    invalid_username = ValueError("{0} is not a valid username".format(key))
                    raise invalid_username
                break
            except ValueError:
                print("Invalid format, try again: ")
        if 0 < key < 101 and re.fullmatch("^[a-z]{1,8}", values):
            dictionary[key] = values
        else:
            return "Invalid inputs for the dictionary"

    return dictionary


# Find a list of keys that contain in the first index the digit.
def returnKeyList():
    digit = input("Set one digit that you want to find: ")
    list = []
    keys_list = dictionary.keys()
    if not re.fullmatch("\d{1}", digit):
        return "Invalid Input"
    for k in keys_list:
        if str(k)[0].find(digit) != -1:
            list.append(k)
    return list


# Find a list of values that contain in the first index the character.
def returnValuesList():
    character = input("Set one character that you want to find: ")
    list = []
    values_list = dictionary.values()
    if not re.fullmatch("\w{1}", character):
        return "Invalid Input"
    for k in values_list:
        if k[0].find(character) != -1:
            list.append(k)
    return list


# Give a dictionary of 1 to 4 groups.
def rangeGroup():
    list_group1 = []
    list_group2 = []
    list_group3 = []
    list_group4 = []

    for k in dictionary:
        if (0 < k < 26):
            print("User belong Group 1")
            list_group1.append(k)
        elif (25 < k < 51):
            print("User belong Group 2")
            list_group2.append(k)
        elif (50 < k < 76):
            print("User belong Group 3")
            list_group3.append(k)
        elif (75 < k < 101):
            print("User belong Group 4")
            list_group4.append(k)

    return {'Group 1': list_group1, 'Group 2': list_group2, 'Group 3': list_group3, 'Group 4': list_group4}


print(createDictionary())
print(returnKeyList())
print(returnValuesList())
print(rangeGroup())
