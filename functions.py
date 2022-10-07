def name():
    return "A thing"

'''
name()
'A thing'

my_thing = name()
my_thing
'A thing'
'''

def greeting(name):
    print(f"{name}, hello to you good sir!")

greeting("kale")
'kale, hello to you good sir!'
greet = greeting("alfie")
'alfie, hello to you good sir!'
'greet = NoneType'

def greeting(name, greeting="hello"):
   return f"{name}, {greeting} to you"

greeting("kale")
'kale, hello to you'

