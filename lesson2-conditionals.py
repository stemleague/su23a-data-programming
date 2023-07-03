age = 10
is_greater_than_10 = (age > 10)  # False
is_less_than_10 = (age < 10)  # False
is_equal_to_10 = (age == 10)  # True
print("Is greater than 10 " + str(is_greater_than_10))
print("Is less than 10 " + str(is_less_than_10))
print("Is equal to 10 " + str(is_equal_to_10))

username = "liz123"
username_is_correct = (username == "elizabeth")
print(username_is_correct)

x = 5
y = 2
# and: means both sides need to be True
# or: means if any left or right expression is True, then it will evaluate to True boolean
exp_1 = (x == 5 and y == 3)
print(exp_1)

# English: If I finish this assignment, I can watch Netflix
finished_assignment = True

if finished_assignment == True:
  print("I can watch Netflix.")
else:  # finished_assignment == False
  print("Please finish your assignment.")
