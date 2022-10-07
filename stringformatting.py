# Strings
course = "Python 3 Crash Course"
print(course[7])
print(course[9:15])

# Lists & Tuples
foods = ["pizza", "cola", "rice"]
print(foods[0])
print(foods[1:]) # to end of list
print(foods[:1]) # beginning to 1
print(foods[1:3])


# String Formatting
name = "Python"
course = "{} for Everybody".format(name)
print(course)

# F Strings
print(f"The crash course language is {name}") #newest
print("Hello %s" % "World") #older
print("Hello %s" % name)