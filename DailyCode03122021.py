# ---------------------------------------------
# #	Daily Code	03/12/2021
#   "Testing K^K == N" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------

# Write a function that returns True if k^k == n for input (n, k) and return False otherwise.

# k_to_k(4, 2) -> True
# k_to_k(387420489, 9) -> True
# 9^9 == 387420489
# k_to_k(3124, 5) -> False
# k_to_k(17, 3) -> False

def k_to_k(n, k):
    solution = k ** k
    if solution == n:
        return True
    else:
        return False

print k_to_k(4, 2)
print k_to_k(387420489, 9)
print k_to_k(3124, 5)
print k_to_k(17, 3)