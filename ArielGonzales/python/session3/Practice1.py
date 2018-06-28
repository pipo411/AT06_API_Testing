dictionary = {}


# Function to create the dictionary, the Function should ask for the length of the dictionary
def createDictionary():
    global dictionary
    tam = int(input("Set the length  for the dictionary: "))
    for i in range(tam):
        key = input("Set your key :")
        value = input("Set your value :")
        dictionary.update({key: value})
    return dictionary


# Return the length
def dictionaryLength(dictionary):
    return len(dictionary)


# Function to print the dictionary keys
def dictionaryKeys(dictionary):
    return dictionary.keys()


# Function to print the dictionary values
def dictionaryValues(dictionary):
    return dictionary.values()


# Function to print the dictionary
def dictionaryItems(dictionary):
    return dictionary.items()


# Function to define is a key inserted by the user, exists on the dictionary.
def existKeyInTheDictionary():
    key = input("Set your key :")
    if dictionary.setdefault(key) == None:
        value = input("Set your value :")
        dictionary.update({key: value})
    else:
        return ("It exist in: ", dictionary.items())
    return dictionary.items()


# Function to define is a value inserted by the user, exists on the dictionary.
def existValueInTheDictionary():
    value = input("Set your value :")
    for keys in dictionary:
        if dictionary.get(keys) == value:
            return ("It exist in: ", dictionary.items())
        else:
            return ("It does not exist in: ", dictionary.items())


print(createDictionary())
print(dictionaryLength(dictionary))
print(dictionaryKeys(dictionary))
print(dictionaryValues(dictionary))
print(dictionaryItems(dictionary))
print(existKeyInTheDictionary())
print(existValueInTheDictionary())
