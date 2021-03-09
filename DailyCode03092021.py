# ----------------------------------------------
# #	Daily Code	03/09/2021
#   "Frames Per Second" Lesson from edabit.com
#   Coded by: Banehowl
# ----------------------------------------------

# Create a function that returns the number of frames shown in a given number of minutes for a certain FPS.

# frames(1, 1) -> 60
# frames(10, 1) -> 600
# frames(10, 25) -> 15000

def frames(minutes, fps):
    minToSeconds = minutes * 60
    solution = minToSeconds * fps
    return solution

print frames(1, 1)
print frames(10, 1)
print frames(10, 25)