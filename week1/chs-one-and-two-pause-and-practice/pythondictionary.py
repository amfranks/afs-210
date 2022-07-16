#Dictionaries are used to store data in key:value pairs where the keys must be unique.

#A dictionary is a collection which is ordered, as of Python version 3.7, changeable (mutable) and does not allow duplicate key values.

#Storing a value using a key that is already in use, results in the old value being replaced with the new value.

#A Dictionary is created by placing a sequence of keys:values pairs, separated by a comma, inside curly brackets {}

#If you are familiar with Javascript, the notation of key:value pairs should be familiar to you as they are similar to JSON data format.

worldCapitals = {
	"Afghanistan" : "Kabul",
	"Bangladesh" : "Dhaka",
	"Canada" : "Ottawa",
	"Cuba" : "Havana",
	"France" : "Paris",
	"Germany" : "Berlin",
	"Philippines" : "Manila",
	"United Kingdom" : "London",
	"United States" : "Washington D.C."
}

# print(worldCapitals.get("France"))
# print(worldCapitals.values())
# print(worldCapitals.keys())

keys = worldCapitals.keys()

# for key in keys:
#     print('"%s" : "%s"' % (key, worldCapitals.get(key)), end=", ")

# print(worldCapitals.items())

# for country, capital in worldCapitals.items():
#     print(country + " = " + capital)

# worldCapitals.pop("Germany")
# print(worldCapitals)

# worldCapitals.update({"United States": "New York"})
# print(worldCapitals)

# worldCapitals.update({"Japan": "Tokyo"}) - Adds key-value pair to dictionary
# print(worldCapitals)

print(worldCapitals.get("Canada")) # Ottawa
print(worldCapitals.setdefault("Canada")) # Ottawa

print(worldCapitals.setdefault("Switzerland", "Bern")) 
print(worldCapitals)