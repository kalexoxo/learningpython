#making a class
class Person:
    pass

kale = Person()
kale
type(kale)
# person

class Person:
    name = "Kale"

kale = Person()
kale.name
#returns = 'Kale' 

# METHODS
class Person:
    def speak(self):
        print("i am hungry")

hungry_person = Person()
hungry_person.speak()
#prints: i am hungry

class Person:
    def __init__(self, name, age, food):
        self.name = name
        self.age = age
        self.food = food
    def speak(self):
        print(f"feed me more {self.food}s")
    def get_name(self):
        print("the name of this person is", self.name)
    def __str__(self):
        return self.name

kale = Person('kale', 21, 'ramen')
kale.speak()
kale.get_name()
print(kale)
