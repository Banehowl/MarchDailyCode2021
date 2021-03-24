# ---------------------------------------------------------------
# #	Daily Code	03/24/2021
#   "Check if objOne is Equal to objTwo" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------------------------

# Create a function that checks to see if two object arguments are equal to one another. Return True if the objects are
# equal, otherwise, return False

# The first object parameter.

obj_one = {
  "name": "Benny",
  "phone": "3325558745",
  "email": "benny@edabit.com"
}

# The second object parameter.

obj_two = {
  "name": "Jason",
  "phone": "9853759720",
  "email": "jason@edabit.com"
}

def is_equal(obj_one, obj_two):
    if obj_one == obj_two:
        return True
    else:
        return False

print is_equal(obj_one, obj_two)
