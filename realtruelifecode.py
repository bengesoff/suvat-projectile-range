import sys

# A list of variables required to work out each variable.
Sh = ("v", "th", "t")
Sv = ("v", "th", "t", "a")
v1 = ("a", "t", "th", "Sv")
v2 = ("a", "t", "th", "Sh")
th1 = ("a", "t", "Sh", "v")
th2 = ("a", "t", "Sv", "v")
a1 = ("v", "t", "Sh", "th")
a2 = ("v", "t", "Sv", "th")
t1 = ("v", "th", "a", "Sv")
t2 = ("v", "th", "a", "Sh")

# Print greeting and valid inputs.
print("Horizontal range (= Sh)")
print("Velocity (= v)")
print("Angle (= a)")
print("Vertical displacement (= Sv)")
print("Time (= t)")
# Tuple of sarkey comments to display when user doesn't enter a valid variable
sarkey = ("Please enter a valid variable", "Please enter a VALID variable... *sighs*", "This is the final time I'm warning you, a VALID variable please...")
i = 0
variable = ""
# Loop 4 times
while i < 4:
    variable = input("Enter the variable you wish to determine:")
    if variable != "Sh" and variable != "v" and variable != "a" and variable != "Sv" and variable != "t":
        if i == 3:
            # Exit program
            sys.exit()
        # Print sarkiness
        print(sarkey[i])
    else:
        # If valid variable is entered, stop asking
        break
    i = i + 1
print("Good choice, I like " + variable + " too!")
