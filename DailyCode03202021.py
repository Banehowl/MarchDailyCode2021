# ------------------------------------------
# #	Daily Code	03/20/2021
#   "Two Makes Ten" Lesson from edabit.com
#   Coded by: Banehowl
# ------------------------------------------

# Create a function that takes two arguments. Both arguments are integers, a and b. Return True if one of them is
# 10 or if their sum is 10.

# makes10(9, 10) -> True
# makes10(9, 9) -> False
# makes10(1, 9) -> True

def makes10(a, b):
    if a == 10 or b ==10:
        return True
    elif a + b == 10:
        return True
    else:
        return False

print makes10(9, 10)
print makes10(9, 9)
print makes10(1, 9)