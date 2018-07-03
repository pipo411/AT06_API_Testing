employee_CE_id = 0
employee_PE_id = 0


def createEmployeID(departament):
    global employee_CE_id
    global employee_PE_id
    if (departament == "commercial"):
        employee_CE_id += 1
        return "CE_" + str(employee_CE_id)
    if (departament == "production"):
        employee_PE_id += 1
        return "PE_" + str(employee_PE_id)


def commercialEmployee(pieces_quantity):
    return int(pieces_quantity) * 2.5


def productionEmployee(effective_pieces, defective_pieces):
    return effective_pieces * 10 + defective_pieces * 1.3


def discountGlobalSalary(global_salary):
    return global_salary * 0.125


def netSalary(global_salary, discount):
    return global_salary - discount
