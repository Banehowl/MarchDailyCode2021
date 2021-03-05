# ----------------------------------------------
# #	Daily Code	03/05/2021
#   "Profitable Gamble" Lesson from edabit.com
#   Coded by: Banehowl
# ----------------------------------------------

# Create a function that takes three arguments prob, prize, pay and returns True if prob * prize > pay; otherwise
# return False

# profitable_gamble(0.2, 50, 9) -> True
# profitable_gamble(0.9, 1, 2) -> False
# profitable_gamble(0.9, 3, 2) -> True

def profitable_gamble(prob, prize, pay):
    profit = prob * prize
    if profit > pay:
        return True
    else:
        return False

print profitable_gamble(0.2, 50, 9)
print profitable_gamble(0.9, 1, 2)
print profitable_gamble(0.9, 3, 2)