numbers = [4, 1, 4, 16, 7, 11, 12, 4, 15]

for n in numbers:
    aux = 0
    i = 1
    while i <= len(numbers):
        if (n % i == 0):
            aux += 1
        i += 1
    if (aux > 2):
        print(n, "Is not a prime number")
    else:
        print(n, "Is a prime number")
