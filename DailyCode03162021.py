# -------------------------------------------------
# #	Daily Code	03/16/2021
#   "Is the String Empty?" Lesson from edabit.com
#   Coded by: Banehowl
# -------------------------------------------------

# Create a function that returns True if a string is empty and False otherwise

# is_empty("") -> True
# is_empty(" ") -> False
# is_empty("a") -> False

def is_empty(s):
    checkString = len(s)
    if checkString == 0:
        return True
    else:
        return False

print is_empty("")
print is_empty(" ")
print is_empty("a")