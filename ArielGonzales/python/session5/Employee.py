from ArielGonzales.python.session5.Person import Person


class Employee(Person):
    employee_id = 0

    def __init__(self, name, last_name, age, ci, departament):
        Employee.employee_id += 1
        self.departament = departament
        Person.__init__(self, name, last_name, age, ci)

    def getEmployeeID(self):
        return self.employee_id

    def getDepartament(self):
        return self.departament


employee1 = Employee("Pam", "Baruch", 75, 657654, "Human Resources")
print(employee1.getName())
print(employee1.getLastName())
print(employee1.getAge())
print(employee1.getCi())
print(employee1.getEmployeeID())
print(employee1.getDepartament())
print("---------------------------------------------------")
employee2 = Employee("Dido", "Morto", 75, 657654, "Security")
print(employee2.getName())
print(employee2.getLastName())
print(employee2.getAge())
print(employee2.getCi())
print(employee2.getEmployeeID())
print(employee2.getDepartament())
