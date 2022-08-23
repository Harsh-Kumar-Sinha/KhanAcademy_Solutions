#Methods like .__init__() and .__str__() are called dunder methods

class Dog:
    species = "Canis familiaris"
        
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

    def __str__(self):
        return f"{self.name} is {self.age} years old"


d1 = Dog("German",12)
d2 = Dog("Sephard",14)

d1.name = "Rocky"
d2.age = 11

print(f"The first dog is {d1.name} and the second dog is {d2.name}")
print(f"The age of first dog is {d1.age} and the age of second dog is {d2.age}")

print(d1.description())
print(d2.description())

#earlier it showed the address of the object and we overridden the address with the value of our own
print(d1)