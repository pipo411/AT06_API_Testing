def sum_to_n(num):
    sum = 0
    i = 1
    while i <= num:
        sum += i
        i += 1
        if (i > 35):
            break

    return sum


print(sum_to_n(10))
print(sum_to_n(5))
print(sum_to_n(40))
print(sum_to_n(35))
print(sum_to_n(100))
