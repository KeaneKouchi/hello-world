# Ask the use to enter a floating point number between 1 and 100
# Square the number and return the value rounded to 2 decimals
# to the user.
# Name: Keane Kouchi
# Date: 9/4/24

value_entered = input("Please enter a whole number between 1 and 100: ")


value_entered = float(value_entered)
value_squared = value_entered**2
print("You entered: ",value_entered)
print("The value squared = ", round(value_squared,2))
