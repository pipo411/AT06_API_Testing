dictionary = {}


# Define a function that can return a dictionary where the keys are numbers between 1 and 9 (both included) and the values are square of keys.
#
# The keys should be inputs and the validation for the max and Min values should be defined.
def createDictionary1_9():
    global dictionary
    tam = int(input("Set the length  for the dictionary: "))
    for i in range(tam):
        key = int(input("Set your key :"))
        if 1 <= key <= 9:
            dictionary.update({key: key ** 2})
        else:
            return "Put a valid kay between 1 to 9"
    return dictionary


# Define a function to print a dictionary that contains all the prime numbers extracted from the previous dictionary.
def primeDictionary(dictionary):
    primeDictionary = {}
    for keys in dictionary:
        if primeNumber(keys):
            primeDictionary.update({keys: keys ** 2})

    return primeDictionary


# Return True if it is a Prime number
def primeNumber(number):
    aux = 0
    i = 1
    while i <= number:
        if number % i == 0:
            aux += 1
        if aux > 2:
            return False
        else:
            return True


print(createDictionary1_9())
print(primeDictionary(dictionary))
