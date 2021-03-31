# -----------------------------------------------------
# #	Daily Code	03/31/2021
#   "Convert Number to Dashes" Lesson from edabit.com
#   Coded by: Banehowl
# -----------------------------------------------------

# Create a function that takes a number (from 1 - 60) and returns a corresponding string of hyphens.

# num_to_dashes(1) -> "-"
# num_to_dashes(5) -> "-----"
# num_to_dashes(3) -> "---"

def num_to_dashes(num):
    translate = "-" * num
    return translate

print num_to_dashes(1)
print num_to_dashes(5)
print num_to_dashes(3)