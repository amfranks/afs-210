# The simplest form of class definition looks like this:
# class ClassName:
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>

class dog:

    def __init__(self, name, breed, age, color, size):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        self.size = size

    def bark(self):
        print("Woof..Woof")

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

dog1 = dog("Max", "German Shepherd", 2, "brown", "large")
dog2 = dog("Cooper", "Labrador", 4, "black", "large")
dog3 = dog("Bella", "Chihuahua", 1, "tan", "small")

print(dog1.getName())
print(dog1.bark())
print(dog1.setAge(3))
print(dog1.getAge())