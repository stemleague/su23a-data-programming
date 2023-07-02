# Command: print() outputs whatever is inside of the parentheses
# print(1)              # int
# print("hello world")  # string
# print(4.0)
# print(True)


age = 20 # int
is_greater_than_10 = age > 10  # 20 > 10 --> True

print("Hi My name is Elizabeth and my age is " + str(age)) # str
# We are combine a string and an integer
# TypeError: can only concatenate str (not "int") to str

print("Hi I'm looking forward to learn about Data Programming")
print("My age in 10 years will be " + str(age + 10)) # expect 20
print("My age in 20 years will be "+ str(age + 20)) # expect 30
print("My age is greater than 10 is " + str(is_greater_than_10)) # expect False
