import sys
print("Horizontal range (= Sh)")
print("Velocity (= v)")
print("Angle (= a)")
print("Vertical displacement (= Sv)")
print("Time (=t)")
variable = input("Enter the variable you wish to determine:")
if variable != "Sh" and variable != "v" and variable != "a" and variable != "Sv" and variable != "t":
    print("Please enter a VALID variable... *sighs*")
if variable != "Sh" and variable != "v" and variable != "a" and variable != "Sv" and variable != "t":
    print("This is the final time I'm warning you, VALID variable")
if variable != "Sh" and variable != "v" and variable != "a" and variable != "Sv" and variable != "t":
    sys.exit()
