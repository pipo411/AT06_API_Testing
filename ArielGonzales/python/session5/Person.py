class Person:
    def __init__(self, name, last_name, age, ci):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.ci = ci

    def getName(self):
        return self.name

    def getLastName(self):
        return self.last_name

    def getAge(self):
        return self.age

    def getCi(self):
        return self.ci
