# -----------------------------------------
# #	Daily Code	03/26/2021
#   "Moving House" Lesson from edabit.com
#   Coded by: Banehowl
# -----------------------------------------

# I'd like to calculate how long on average I've lived in the same house.

# Given a person's age and the number of times they've moved house as moves, return the average number of years
# that they've spent living in the same house.

# years_in_one_house(30, 1) -> 15
# years_in_one_house(15, 2) -> 5
# years_in_one_house(80, 0) -> 80

def years_in_one_house(age, moves):
    averageYears = age / (moves + 1)
    return averageYears

print years_in_one_house(30, 1)
print years_in_one_house(15, 2)
print years_in_one_house(80, 0)