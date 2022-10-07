print("Hello World")
print(3**3) #power of

#variables
name = "Python"
print(name)

#indentation
if name == "Python":
    print("Your name is Python")

#data types
type(name) #string

# list
groceries = ["milk", "eggs", "ice cream"]
print(type(groceries))
print(groceries)

# dictionary : used to store similar data
person = {
    'key' : 'value',
    'name' : 'kale',
    'language': 'python'
}
print(type(person))
print(person)
person['name'] # returns 'kale'
person['language'] # returns python

# tuples : a list u cannot change, cannot remove or add variable
kids = ('Ashley', 'Nathan', 'Evie', 'Noah')
print(type(kids))
print(kids)

# set : can add/remove items, unique items 
foods = {'pizza', 'ramen', 'cheesecake', 'pizza', 'pizza', 'ramen'}
print(type(foods))
print(foods) # only show pizza and ramen one time

# booleans : t/f
is_adult = True
print(type(is_adult))

# NoneType
total = None
print(type(total))
