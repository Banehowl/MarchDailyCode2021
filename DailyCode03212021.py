# -----------------------------------------------------------------
# #	Daily Code	03/21/2021
#   "Sum of List Less Than 100 List Remix" Lesson from edabit.com
#   Coded by: Banehowl
# -----------------------------------------------------------------

# Given a list of numberes, return True if the sum of the values in the list is less than 100; otherwise return False

# list_less_than_100([5, 57]) -> True
# list_less_than_100([77, 30]) -> False
# list_less_than_100([0]) -> True

def list_less_than_100(lst):
    lstSum = sum(lst)
    if lstSum < 100:
        return True
    else:
        return False

print list_less_than_100([5, 57])
print list_less_than_100([77, 30])
print list_less_than_100([0])