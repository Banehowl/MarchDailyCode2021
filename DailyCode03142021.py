# -------------------------------------------------------------------
# #	Daily Code	03/14/2021
#   "Compare Strings by Count of Characters" Lesson from edabit.com
#   Coded by: Banehowl
# -------------------------------------------------------------------

# Create a function that takes two strings as arguments and returns either True or False depending on whether the
# total number of characters in the first string is equal to the total number of characters in the second string.

# comp("AB", "CD") -> True
# comp("ABC", "DE") -> False
# comp("hello", "edabit") -> False

def comp(txt1, txt2):
    lengthText1 = len(txt1)
    lengthText2 = len(txt2)
    if lengthText1 == lengthText2:
        return True
    else:
        return False

print comp("AB", "CD")
print comp("ABC", "DE")
print comp("hello", "edabit")