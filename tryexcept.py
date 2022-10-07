try:
    pass
except:
    pass

# 1/0 == division by 0 error

try:
    1/0
except Exception as e:
    print(e)
    print(type(e))

try:
    1/0
except Exception as e:
    print(e)
    print(type(e))
    print("this still runs")

try:
    10/0
    print("show me")
except ZeroDivisionError:
    print("cannot divide by 0")
print("...program still runs normally")
