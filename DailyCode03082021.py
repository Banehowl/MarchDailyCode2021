# -------------------------------------------------------------
# #	Daily Code	03/08/2021
#   "Get the Sum of All List Elements" Lesson from edabit.com
#   Coded by: Banehowl
# -------------------------------------------------------------

# Create a function that takes a list and returns the sum of all numbers in the list

# get_sum_of_elements([2, 7, 4]) -> 13
# get_sum_of_elements([45, 3, 0]) -> 48
# get_sum_of_elements([-2, 84, 23]) -> 105

def get_sum_of_elements(lst):
    total = sum(lst)
    return total

print get_sum_of_elements([2, 7, 4])
print get_sum_of_elements([45, 3, 0])
print get_sum_of_elements([-2, 84, 23])