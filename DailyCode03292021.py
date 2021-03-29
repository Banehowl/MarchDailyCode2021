# ------------------------------------------------
# #	Daily Code	03/29/2021
#   "Buggy Code (Part 3)" Lesson from edabit.com
#   Coded by: Banehowl
# ------------------------------------------------

# Fix the code in the code tab to pass this challenge (only syntax errors).
# Look at the examples below to get an idea of what the function should do.

# sum_lst([1, 2, 3, 4, 5]) -> 15
# sum_lst([-1, 0, 1]) -> 0
# sum_lst([0, 4, 8, 12]) -> 24

# def sum_lst(lst):
# 	total
# 	for i in range(0,lst):
# 		total += lst[i]
#   return total

def sum_lst(lst):
    total = sum(lst)
    return total

print sum_lst([1, 2, 3, 4, 5])
print sum_lst([-1, 0, 1])
print sum_lst([0, 4, 8, 12])