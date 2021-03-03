# --------------------------------------------------------------
# #	Daily Code	03/03/2021
#   "Return the Last element in a List" Lesson from edabit.com
#   Coded by: Banehowl
# --------------------------------------------------------------

# Create a function that accepts a list and returns the last iem in the list. The list can be either homogeneous
# or hetrogeneous.

# get_last_item([1, 2, 3]) -> 3
# get_last_item(["cat", "dog", "duck"]) -> "duck"
# get_last_item([True, False, True]) -> True
# get_last_item([7, "String", False]) -> False

def get_last_item(lst):
    lastitem = lst[-1]
    return lastitem

print get_last_item([1, 2, 3])
print get_last_item(["cat", "dog", "duck"])
print get_last_item([True, False, True])
print get_last_item([7, "String", False])
