a = 1
b = 2
c = 3
d = 4
e = 0
f = 1
g = 1
aux = 0

# Using the assignment operator =
x = a + b + d
print(x)

# Using the assignment operator += & -=
while (x > 0):
    e += 4
    x -= 1
print(e)

# Using the assignment operator *= & -=
while (x > -2):
    f *= d
    x -= 1
print(f)

# Using the assignment operator /= & -=
while (aux < d):
    g /= b
    aux += 1
print(g)
