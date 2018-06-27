pi = 3.14159


def area_of_circle(radio):
    if (radio > 10):
        return pi * radio ** 2
    else:
        return "Is not more than 10"

print("The area of is",area_of_circle(15))
print(area_of_circle(1))
