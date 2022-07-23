# Data1 = 7, False, "Apple", True, 7, 98.6 
# Data2 = "July", 4, 8, "Tango", 4.3, "Bingo"
# Data3 = "A", 7, -1, 3.14, True, 7  
# Data4 =  "name" = "Joe",  "age" = 26,   "active" = True,  "hourly_wage" = 14.75

########################################################################

# Data1 - Count the number of items
# Data1 - Find the value of the fourth item stored in the data set
# Data1 - Count the number of times 7 appears
data1 = (7, False, "Apple", True, 7, 98.6)
print(len(data1))
print(data1.index(True))
print(data1.count(7))


# Data2 - Remove a random element from the data set
# Data2 - Add "Alpha" to the data set
# Data2 - Print data set
data3 = {"A", 7, -1, 3.14, True, 7}  
data3.pop()
data3.add("Alpha")
print(data3)


# Data3 - Print the data set in reverse order
# Data3 - Change the second value in the data set to ‘B’
# Data3 - Remove the last item and print the data set
data3 = ["A", 7, -1, 3.14, True, 7]
data3.reverse()
data3.pop()
print(data3)


# Data4 - Change "active" to False
# Data4 - Add "address" with a value of "123 West Main Street"
# Data4 - Print the weekly salary for Joe if he worked a full 40 hour week.
# Data4 - Print the data set
data4 =  {"name": "Joe", "age": 26, "active": True, "hourly_wage": 14.75}
data4.update({"address": "123 West Main Street"})
weeklySalary = data4["hourly_wage"] * 40
print(weeklySalary)
print(data4)