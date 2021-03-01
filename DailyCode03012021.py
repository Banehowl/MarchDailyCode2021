# -----------------------------------------------
# #	Daily Code	03/01/2021
#   "Maximum Difference" Lesson from edabit.com
#   Coded by: Banehowl
# -----------------------------------------------

# Given a list of integers, return the difference between the largest and smallest integers in the list

# difference([10, 15, 20, 2, 10, 6]) -> 18
# 20 - 2 = 18

# difference([-3, 4, -9, -1, -2, 15]) -> 24
# 15 - (-9) = 24

# difference([4, 17, 12, 2, 10, 2]) -> 15

def difference(nums):
    largeNum = max(nums)
    smallNum = min(nums)
    solution = largeNum - smallNum
    return solution

print difference([10, 15, 20, 2, 10, 6])
print difference([-3, 4, -9, -1, -2, 15])
print difference([4, 17, 12, 2, 10, 2])