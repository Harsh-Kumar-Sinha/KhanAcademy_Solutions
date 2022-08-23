class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class GoldenRetriever(Dog):

    def speak(self,sound="Bark"):
        return f"{self.name} says {sound}"


d1 = Dog("Rocky",12)
print(d1)
print(d1.speak("woof"))


Gr = GoldenRetriever("Panthur",20)
print(Gr)
print(Gr.speak())