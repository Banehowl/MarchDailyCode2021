# ---------------------------------------------------------------------
# #	Daily Code	03/17/2021
#   "Front 3 - Slice Check Repeat Concatenate" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------------------------------

# Create a function that takes a string; we'll say that the front is the first three characters of the string.
# If the string length is less than three characters, the front is whatever is there.
# Return a new string, which is three copies of the front.

# front3("Python") -> "PytPytPyt"
# front3("Cucumber") -> "CucCucCuc"
# front3("bioshock") -> "biobiobio"

def front3(txt):
    sliceObj = slice(0,2)
    sliceTxt = txt[sliceObj]
    repeatTxt = sliceTxt + sliceTxt + sliceTxt
    return repeatTxt

print front3("Python")
print front3("Cucumber")
print front3("bioshock")