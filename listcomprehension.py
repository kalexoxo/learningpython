nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("nums:", nums)

times_ten = [num for num in nums]
print("unchanged:", times_ten)

times_ten = [num*10 for num in nums]
print("x 10:", times_ten)

times_ten = [num*10 for num in nums if num % 2 == 0]
print("even numbers x 10:", times_ten)