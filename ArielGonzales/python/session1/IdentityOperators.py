# Indetity Operators
a = "DOG"
b = "DOG"

# verify if a & b are the same object
if (a is b):
    print("a and b are the same object")
else:
    print("a and b are not the same object")

# verify if a & b are not the same object
b = "BIRD"
if (a is b):
    print("a and b are the same object")
else:
    print("a and b are not the same object")

# verify if a & b are the same object
if (a is not b):
    print("a and b are the same object")
else:
    print("a and b are not the same object")
