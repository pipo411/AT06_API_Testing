import re

from ArielGonzales.python.Examen import Salary
from ArielGonzales.python.Examen.Employee import Employee

company_employees = {}


def setEmployees():
    global company_employees
    employees = {}
    while True:
        try:
            amount = int(input("Set the amount of employees: "))
            if not 2 < amount < 16:
                error_employees = ValueError("The amount {} is wrong".format(amount))
                raise error_employees
            break
        except ValueError:
            print("Invalid amount of employees, try again")
    for i in range(amount):
        while True:
            try:
                employee_name = input("Set the name: ")
                department = input("Set the departament: ")
                if not re.fullmatch("^[a-zA-z]+", employee_name):
                    error_employee_format = ValueError("The uername format {} is wrong".format(employee_name))
                    raise error_employee_format
                if not (department == "commercial" or department == "production"):
                    error_employees_department = ValueError("The uername format {} is wrong".format(department))
                    raise error_employees_department
                break
            except ValueError:
                print("Invalid format of employees, try again")

        globalSalary = 0
        if (department == "commercial"):
            globalSalary = askPiecesQuantityCommercial()
            # company_employees[company_employees[i].getEmployeeIDCE()]

        elif department == "production":
            globalSalary = askPiecesQuantityProduction()
        discount = Salary.discountGlobalSalary(globalSalary)
        print(Salary.createEmployeID(department))
        employees[i] = Employee(employee_name, department, Salary.createEmployeID(department), globalSalary, discount
                                , Salary.netSalary(globalSalary, discount))

    return buildAnswer(employees)


def askPiecesQuantityCommercial():
    pieces_quantity = int(input("The pieces quantity for commercial employee: "))
    return pieces_quantity


def askPiecesQuantityProduction():
    efective_pieces = int(input("The efective pieces quantity for production employee: "))
    defective_pieces = int(input("The defective pieces quantity for production employee: "))
    return Salary.productionEmployee(efective_pieces, defective_pieces)


def buildAnswer(employee):
    resp = ""
    list = []
    for e in employee:
        resp = "UserId {}" \
               ", Username {}" \
               ", Departmenet {}" \
               ", Global Salary {}" \
               ", Total Discount {}" \
               ", Net Salary {} ".format(employee[e].getEmployeeID(),
                                         employee[e].getName(),
                                         employee[e].getDepartment(),
                                         employee[e].getGlobalSalary(),
                                         employee[e].getDiscount(),
                                         employee[e].getNetSalary())
        list.append(resp)

    return list


print(setEmployees())
