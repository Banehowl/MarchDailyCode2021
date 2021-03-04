# --------------------------------------------------------------
# #	Daily Code	03/04/2021
#   "Name Greeting!" Lesson from edabit.com
#   Coded by: Banehowl
# --------------------------------------------------------------

# Create a function that takes a name and returns a greeting in the form of a string.

# hello_name("Gerald") -> "Hello Gerald!"
# hello_name("Tiffany") -> "Hello Tiffany!"
# hello_name("Ed") -> "Hello Ed!"

def hello_name(name):
    greet = "Hello %s!" % name
    return greet

print hello_name("Gerald")
print hello_name("Tiffany")
print hello_name("Ed")
