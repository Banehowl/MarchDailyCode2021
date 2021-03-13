# ------------------------------------------------
# #	Daily Code	03/13/2021
#   "Buggy Code (Park 2)" Lesson from edabit.com
#   Coded by: Banehowl
# ------------------------------------------------

# Fix the code in the code tab to pass this challenge (only syntax errors)

# max_num(3, 7) -> 7
# max_num(-1, 0) -> 0
# max_num(1000, 400) -> 1000

# def max_num(n1, n2):
# 	if n1 > n2:
# 		return n2
# 	elif:
# 		return n1

def max_num(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

print max_num(3, 7)
print max_num(-1, 0)
print max_num(1000, 400)