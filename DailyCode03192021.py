# --------------------------------------------
# #	Daily Code	03/19/2021
#   "Return Negative" Lesson from edabit.com
#   Coded by: Banehowl
# --------------------------------------------

# Create a function that takes a number as an argument and returns negative of that number. Return negative
# numbers without any change.

# return_negative(4) -> -4
# return_negative(15) -> -15
# return_negative(-4) -> -4
# return_negative(0) -> 0

def return_negative(n):
    if n > 0:
        negativeNum = n * -1
        return negativeNum
    else:
        return n

print return_negative(4)
print return_negative(15)
print return_negative(-4)
print return_negative(0)