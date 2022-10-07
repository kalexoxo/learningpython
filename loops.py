groceries = ["milk", "eggs", "ice cream"]

# for loops
for item in groceries:
    print(f"the item is {item}")

# iterables : SET, TUPLE, STRING, LIST...

name = " Python 3 Crash Course"
name = name.strip()  #took spaces off of string
print(name)

for letter in name:
    l = letter.lower()
    if l in 'iaeiouy':
        print(f"vowel is: {l}")
        continue


for letter in name:
    l = letter.lower()
    if l in 'iaeiouy':
        print(f"vowel is: {l}")
        continue
    if l == "3" :
        print("breaking on 3")
        break


# while loops
num = 0
while num < 10:
    print(num)
    num = num + 1

