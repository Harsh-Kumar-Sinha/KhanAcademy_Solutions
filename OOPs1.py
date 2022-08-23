class employee:
    
    #class attribute
    company_name = "Abzooba India Infotech Pvt Ltd"

    #instance methods and name,age,pos,yoj are called instance attribute
    def __init__(self,name,age,pos,yoj):
        self.name = name
        self.age = age
        self.pos = pos
        self.yoj = yoj

    def details(self):
        print(f"Name : {self.name}\nAge : {self.age}\nDesignation : {self.pos}\nYear Of Joining : {self.yoj}")


emp1 = employee("Harsh",23,"Trainee-DS",2022)
emp2 = employee("Ankur",22,"DSE",2022)

print(emp1)
emp1.details()

print(emp2)
emp2.details()

print(emp1 == emp2)

print(emp1.yoj == emp2.yoj)

print(emp1.company_name)
print(emp2.company_name)