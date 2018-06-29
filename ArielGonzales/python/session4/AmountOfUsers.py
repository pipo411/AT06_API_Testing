from python.session4.modulos import CalculateMinuteHourDay, WhatAreYou

dictionary = {}


def users():
    global dictionary
    amount_of_users = int(input("Put the amount of users: "))
    for i in range(amount_of_users):
        name = input("Put the name: ")
        age = int(input("Put the age: "))
        dictionary[name] = age
    return buildAnswer()


def calculateTime(elements):
    text = []
    text.append(CalculateMinuteHourDay.convertToDay(dictionary.get(elements)))
    text.append(CalculateMinuteHourDay.convertToHour(dictionary.get(elements)))
    text.append(CalculateMinuteHourDay.convertToMinute(dictionary.get(elements)))
    return text


def whatDoTheyAre(elements):
    return WhatAreYou.whatAreYou(dictionary.get(elements))


def buildAnswer():
    text = []
    for elements in dictionary:
        text.append(elements)
        text.append(calculateTime(elements))
        text.append(whatDoTheyAre(elements))
    return text


print(users())
