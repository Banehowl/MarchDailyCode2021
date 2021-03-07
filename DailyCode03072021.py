# ------------------------------------------
# #	Daily Code	03/07/2021
#   "Perfect Roots" Lesson from edabit.com
#   Coded by: Banehowl
# ------------------------------------------

# Given a number n, find if its 2nd, 4th, and 8th roots are all integers (perfect roots), return True if it exist,
# False if not.

# perfect_roots(256) -> True
# # 2nd root of 256 is 16
# # 4th root of 256 is 4
# # 8th root of 256 is 2
#
# perfect_roots(1000) -> False
# perfect_roots(6561) -> True

def perfect_roots(n):
    firstCheck = (n ** .5) % 2
    secondCheck = (n ** .25) % 2
    thirdCheck = (n ** .125) % 2
    if firstCheck == 0 and secondCheck == 0 and thirdCheck == 0:
        return True
    else:
        return False

print perfect_roots(256)
print perfect_roots(1000)
print perfect_roots(6561)