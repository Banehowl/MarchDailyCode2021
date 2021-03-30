# ------------------------------------------------
# #	Daily Code	03/30/2021
#   "Basic Calculator (Part 3)" Lesson from edabit.com
#   Coded by: Banehowl
# ------------------------------------------------

# Create a function that takes two numbers and a mathematical operator and will perform a caluclation with the
# given numbers.

# calculator(2, "+", 2) -> 4
# calculator(2, "*", 2) -> 4
# calculator(4, "/", 2) -> 2

def calculator(num1, operator, num2):
    if operator == "+":
        calc = num1 + num2
        return calc
    elif operator == "-":
        calc = num1 - num2
        return calc
    elif operator == "*":
        calc = num1 * num2
        return calc
    elif operator == "/":
        if num2 == 0:
            return "Not divisable by 0!"
        else:
            calc = num1 / num2
            return calc

print calculator(2, "+", 2)
print calculator(2, "*", 2)
print calculator(4, "/", 2)
print calculator(4, "/", 0)