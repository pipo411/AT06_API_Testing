def days_in_month(month):
    months = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 30,
        "September": 31,
        "October": 30,
        "November": 31,
        "December": 30
    }
    if (month not in months):
        return None
    else:
        return months.get(month)


print("May has", days_in_month("May"), "days")
print("September has", days_in_month("September"), "days")
print("December has", days_in_month("December"))
print("February has", days_in_month("February"), "days")
print("April has", days_in_month("April"), "days")
print(days_in_month("Duck"))
