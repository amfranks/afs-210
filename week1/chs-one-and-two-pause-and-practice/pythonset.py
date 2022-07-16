#In a Set, items are unordered, un-indexed and do not allow duplicate values.

#Unordered means that the items in a set do not have a defined order.

#This means that items in a Set can appear in a different order every time you use them, and cannot be referenced by an index or key.

#Sets cannot have two items with the same value.

#A Set is created by placing a sequence of values separated by a comma inside curly brackets {}

progLang = {"python", "c#", "javascript", "java", "c++"}
moreLang = {"rust", "php", "perl", "ruby", "go", "java", "python"}

myNumbers = {1, 2, 3, 4, 5}
myFloats = {1.0, 2.1, 3.2, 4.3}

progLang.add("python")
removedItem = progLang.pop()
# print(progLang)
# print(removedItem)
# progLang.discard("c#")
# print(progLang)
progLang.remove("c#")

print(progLang.difference(moreLang))
print(moreLang.difference(progLang))
print(progLang.intersection(moreLang))