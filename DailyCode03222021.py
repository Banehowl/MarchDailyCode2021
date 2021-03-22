# -------------------------------------------------------
# #	Daily Code	03/22/2021
#   "Is the String Odd or Even?" Lesson from edabit.com
#   Coded by: Banehowl
# -------------------------------------------------------

# Given a string, return True if its length is even or False if the length is odd.

# odd_or_even("apples") -> True
# odd_or_even("pears") -> False
# odd_or_even("cherry") -> True

def odd_or_even(word):
    wordLen = len(word)
    if wordLen % 2 == 0:
        return True
    else:
        return False

print odd_or_even("apples")
print odd_or_even("pears")
print odd_or_even("cherry")