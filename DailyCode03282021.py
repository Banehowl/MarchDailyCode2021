# ------------------------------------------------
# #	Daily Code	03/28/2021
#   "Buggy Code (Part 4)" Lesson from edabit.com
#   Coded by: Banehowl
# ------------------------------------------------

# Emmy has written a function that returns a greeting to users. However, she's in love with Mubashir,
# and would like to greet him slightly differently. She added a special case in her function, but she made a mistake.
# Can you help her?

# def greeting(name):
# 	return "Hello, " + name + "!"
# 	if name == "Mubashir":
# 		return "Hello, my Love!"

# greeting("Matt") -> "Hello, Matt!"
# greeting("Helen") -> "Hello, Helen!"
# greeting("Mubashir") -> "Hello, my Love!"

def greeting(name):
    if name == "Mubashir":
        return "Hello, my Love!"
    else:
        return "Hello, " + name + "!"

print greeting("Matt")
print greeting("Helen")
print greeting("Mubashir")