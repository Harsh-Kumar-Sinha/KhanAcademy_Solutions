# Single inheritance -- child(father)
# Multilevel inheritance -- father(grandfather)  child(father)
# multiple inheritance -- child(father,mother)
# Hierarchical  inheritance -- child1(father) child2(father)

class grandparent:
    def __init__(self,name):
        self.name = name

    def calm(self):
        print("Meditates daily")

class father(grandparent):
    def __init__(self,name):
        self.name = name
    
    def work(self):
        print("works outside")

    def anger(self):
        print("Nature is angry")

class mother:
    def __init__(self,name):
        self.name = name
    
    def work(self):
        print("works inside")

    def anger(self):
        print("Nature is caring")

    def cooking(self):
        print("Loves cooking")

class child1(mother,father):
    def __init__(self,name):
        self.name = name
    
    def play(self):
        print("Loves Playing")

class child2(mother):
    def __init__(self,name):
        self.name = name
    
    def play(self):
        print("Loves Playing")

g = grandparent("Late Saktidhar Sinha")
f = father("Sunil Kr Sinha")
m = mother("Kamalika Sinha")
c = child1("Ayush")
c2 = child2("Harsh")

# single inheritance from grandparent to father
#multilevel inheritance from grandparent to child
g.calm()
f.calm() 
c.calm() 

#multiple inheritance of child from father and mother
c.cooking() 
c.work()

#This conflict is solved by MRO by taking the function of the leftmost class's property
#child(father,mother) so father's angry property is chosen
#child(mother,father) so mother's angry property is chosen
c.anger()

c2.cooking()