class Employee:
    def __init__(self, firstName, lastName, employeeID, hourlyPay):
        self.firstName = firstName
        self.lastName = lastName
        self.employeeID = employeeID
        self.hourlyPay = hourlyPay

    def pay(self, ttlHrsWorked):
        weeklyPay = float(self.hourlyPay) * float(ttlHrsWorked)

        if (float(ttlHrsWorked) <= 40):
            return round(weeklyPay, 2)
        elif (float(ttlHrsWorked) > 40):
            # additionalHours = float(ttlHrsWorked) - 40
            additionalHoursPay = weeklyPay + (1.5 * float(self.hourlyPay))
            return round(additionalHoursPay, 2)

employeeID = input("Please enter the Employee's ID: ")
employeeFirstName = input("Please enter the Employee's First Name: ")
employeeLastName = input("Please enter the Employee's Last Name: ")
employeeHourlyPay = input("Please enter the Employee's Hourly Pay Rate: ")
hrsWorkedThisWeek = input(f"How many hours did {employeeFirstName} work this week?: ")

employee1 = Employee(employeeFirstName, employeeLastName, employeeID, employeeHourlyPay)

print(f"${employee1.pay(hrsWorkedThisWeek)}")