# ----------------------------------------------------------------------------
# #	Daily Code	03/23/2021
#   "Concatenate First and Last Name into One String" Lesson from edabit.com
#   Coded by: Banehowl
# ----------------------------------------------------------------------------

# Given two strings, first_name and last_name, return a single string in the format "last, first"

# concat_name("First", "Last") -> "Last, First"
# concat_name("John", "Doe") -> "Doe, John"
# concat_name("Mary", "Jane") -> "Jane, Mary"

def concat_name(first_name, last_name):
    lastFirst = last_name + ", " + first_name
    return lastFirst

print concat_name("First", "Last")
print concat_name("John", "Doe")
print concat_name("Mary", "Jane")