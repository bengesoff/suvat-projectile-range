import sys
print("Horizontal range (= Sh)")
print("Velocity (= v)")
print("Angle (= a)")
print("Vertical displacement (= Sv)")
print("Time (= t)")
sarkey = ("Please enter a valid variable", "Please enter a VALID variable... *sighs*", "This is the final time I'm warning you, a VALID variable please...")
i = 0
variable = ""
while i < 4:
    variable = input("Enter the variable you wish to determine:")
    if variable != "Sh" and variable != "v" and variable != "a" and variable != "Sv" and variable != "t":
        if i == 3:
            sys.exit()
        print(sarkey[i])
    else:
        break
    i = i + 1
print("Good choice, I like " + variable + " too!")
