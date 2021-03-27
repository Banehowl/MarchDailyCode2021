# --------------------------------------------------------------
# #	Daily Code	03/27/2021
#   "Area of a Rectange w/ a Condition" Lesson from edabit.com
#   Coded by: Banehowl
# --------------------------------------------------------------

# Create a function that calculates the area of a rectangle. If the arguments are invalid,
# your function must return -1.

# area(3, 4) -> 12
# area(10, 11) -> 110
# area(-1, 5) -> -1
# area(0, 2) -> -1

def area(x, y):
    if x < 0:
        return -1
    elif y < 0:
        return -1
    else:
        recArea = x * y
        return recArea

print area(3, 4)
print area(10, 11)
print area(-1, 5)
print area(0, 2)
