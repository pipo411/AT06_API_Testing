from ArielGonzales.python.Examen.Person import Person


class Employee(Person):
    def __init__(self, employee_name, department, employeID, globalSalary, discount, netSalary):
        self.department = department
        self.employeID = employeID
        self.globalSalary = globalSalary
        self.discount = discount
        self.netSalary = netSalary
        Person.__init__(self, employee_name)

    def getDepartment(self):
        return self.department

    def getEmployeeID(self):
        return self.employeID

    def getGlobalSalary(self):
        return self.globalSalary

    def getDiscount(self):
        return self.discount

    def getNetSalary(self):
        return self.netSalary
