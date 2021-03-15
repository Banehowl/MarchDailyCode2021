# -------------------------------------------
# #	Daily Code	03/15/2021
#   "Divides Evenly" Lesson from edabit.com
#   Coded by: Banehowl
# -------------------------------------------

# Given two integers, a and b, return True if a can be divided evenly by b. Return False otherwise

# divides_evenly(98, 7) -> True
# 98/7 = 14

# divides_evenly(85, 4) -> False
# 85/4 = 21.25

def divides_evenly(a, b):
    checkRemainder = a % b
    if checkRemainder == 0:
        return True
    else:
        return False

print divides_evenly(98, 7)
print divides_evenly(85, 4)
