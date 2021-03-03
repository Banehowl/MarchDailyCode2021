# -----------------------------------------------
# #	Daily Code	03/02/2021
#   "Less Than 100?" Lesson from edabit.com
#   Coded by: Banehowl
# -----------------------------------------------

# Given two numbers, return True if the sum of both numbers is less than 100. Otherwise return False.

# less_than_100(22, 15) -> True
# 22 + 15 = 37

# less_than_100(83, 34) -> False
# 83 + 34 = 117

# less_than_100(3, 77) -> true

def less_than_100(x, y):
    sumNum = x + y
    if sumNum < 100:
        return True
    else:
        return False

print less_than_100(22, 15)
print less_than_100(83, 34)
print less_than_100(3, 77)