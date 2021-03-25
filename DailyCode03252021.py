# ---------------------------------------------------------
# #	Daily Code	03/25/2021
#   "List From a Range of Numbers" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------------------

# Create a function that returns a list of all integers between two given numbers start and end

# range_of_num(2, 4) -> [3]
# range_of_num(5, 9) -> [6, 7, 8]
# range_of_num(2, 11) -> [3, 4, 5, 6, 7, 8, 9, 10]

def range_of_num(start, end):
    rangeList = range(start + 1, end)
    return rangeList

print range_of_num(2, 4)
print range_of_num(5, 9)
print range_of_num(2, 11)