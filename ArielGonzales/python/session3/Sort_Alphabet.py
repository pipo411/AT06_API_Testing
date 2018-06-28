# Write a program that reads a string and returns a table of the letters of the alphabet in alphabetical
# order which occur in the string together with the number of times each letter occurs.
# Case should be ignored. A sample output of the program when the user enters the data

def alphabetSort(text):
    dictionary = {}
    cont = 1
    for i in range(len(text)):
        if text[i] != " " and "a" <= text[i] <= "z":
            if dictionary.setdefault(text[i]) == None:
                dictionary.update({text[i]: cont})
            else:
                dictionary.update({text[i]: dictionary.get(text[i]) + 1})
    list = dictionary.items()
    return sorted(list)


print(alphabetSort("banana"))
print(alphabetSort("ban ana"))
print(alphabetSort("Test a StrinG"))
print(alphabetSort("ThiS is String with Upper and lower case Letters"))
