# ---------------------------------------------------------------------------
# #	Daily Code	03/18/2021
#   "Recursion to Repeat a String n Number of Times" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------------------------------------

# Create a recursive function that takes two parameters and repeats the string n number of times.
# The first parameter txt is the string to be repeated and the second parameter is the number of times the
# string is to be repeated.

# repetition("ab", 3) -> "ababab"
# repetition("kiwi", 1) -> "kiwi"
# repetition("cherry", 2) -> "cherrycherry"

def repetition(txt, n):
    for i in range(n):
        newTxt = txt + txt
        return newTxt

print repetition("ab", 3)
print repetition("kiwi", 1)
print repetition("cherry", 2)