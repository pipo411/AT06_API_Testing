def convertToMinute(age):
    return convertToHour(age) * 60


def convertToHour(age):
    return convertToDay(age) * 24


def convertToDay(age):
    return age * 365


