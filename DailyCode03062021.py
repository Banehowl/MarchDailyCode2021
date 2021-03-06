# ---------------------------------------------------------------------
# #	Daily Code	03/06/2021
#   "Check if an Integer is Divisible By Five" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------------------------------

# Create a function that returns True if an integer is evenly divisible by 5, and Flase otherwise.

# divisible_by_five(5) -> True
# divisible_by_five(-55) -> True
# divisible_by_five(37) -> False

def divisible_by_five(num):
    remainder = num % 5
    if remainder == 0:
        return True
    else:
        return False

print divisible_by_five(5)
print divisible_by_five(-55)
print divisible_by_five(37)