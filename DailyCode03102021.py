# --------------------------------------------
# #	Daily Code	03/10/2021
#   "Multiple of 100" Lesson from edabit.com
#   Coded by: Banehowl
# --------------------------------------------

# Create a function that takes an integer and return True if divisible by 100, otherwise return False

# divisible(1) -> False
# divisible(1000) -> True
# divisible(100) -> True

def divisible(num):
    remainder = num % 100
    if remainder == 0:
        return True
    else:
        return False

print divisible(1)
print divisible(1000)
print divisible(100)
