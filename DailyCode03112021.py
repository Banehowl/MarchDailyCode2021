# ----------------------------------------------------
# #	Daily Code	03/11/2021
#   "Using the "and" Operator Lesson from edabit.com
#   Coded by: Banehowl
# ----------------------------------------------------

# Python has a logical operator "and". The "and" Operator takes two bollean values, and returns True if both values are
# True.

# And(True, False) -> False
# And(True, True) -> True
# And(False, True) -> False
# And(False, False) -> False

def And(a, b):
    if a == True and b == True:
        return True
    else:
        return False

print And(True, False)
print And(True, True)
print And(False, True)
print And(False, False)