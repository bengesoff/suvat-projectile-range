import sys
import math

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

def ask_initial_input():
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
    return variable
  
def velocity():
    # function for finding the projectile's velocity
    while True:
        # Determine which equation to use
        i = input("Enter the letter h if you know the horizontal range of your projectile, or letter v if you know the vertical displacement.")
        if i == "h":
            # Constant for average accleration due to gravity
            acceleration = 9.80665
            # Ask user for required variables
            time = float(input("Please enter the time for which your projectile is in the air"))
            angle = float(input("Please enter the angle at which your projectile is launched"))
            horizontal_range = float(input("Please enter the range your projectile travelled, for which I shall circumstantially be very upset if you do not know it"))
            return (0.5 * acceleration * (time ** 2) + horizontal_range) / (math.cos(angle.radians()) * time)
            break
        elif i == "v":
            # Constant for average accleration due to gravity
            acceleration = 9.80665
            # Ask user for required variables
            time = float(input("Please enter the time for which your projectile is in the air"))
            angle = float(input("Please enter the angle at which your projectile is launched"))
            vertical_displacement = float(input("Please enter the vertical displacement that your projectile travelled, for which I shall circumstantially be very upset if you do not know it"))
            return (0.5 * acceleration * (time ** 2) + vertical_displacement) / (math.sin(angle.radians()) * time)
            break
        else:
            print("No you silly... enter v or h, otherwise this message will monotonously repeat itslef until you desist")
def horizontal_range():
    # Ask user for required variables
    velocity = float(input("Please enter the initial velocity of your projectile. [m/s]"))
    angle = float(input("Please enter the angle at which your projectile is being fired. [degrees]"))
    time = float(input("Please enter the time that your projectile will be in the air for. [seconds]"))
    # Calculate v.cos(th).t
    return velocity * math.cos(math.radians(angle)) * time
    
def vertical_displacement():
    # Ask user for required variables
    acceleration = 9.80665
    velocity = float(input("Please enter the initial velocity of your projectile. [m/s]"))
    angle = float(input("Please enter the angle at which your projectile is being fired. [degrees]"))
    time = float(input("Please enter the time that your projectile will be in the air for. [seconds]"))
    # Calculate v.sin(th).t + 0.5.a.t^2
    return (velocity * math.sin(math.radians(angle)) * time) + (0.5 * acceleration * (time ** 2))


variable = ask_initial_input()
if variable == "Sh":
    print("The horizontal range of your projectile will be: " + str(round(horizontal_range(), 3)) + "m")
if variable == "Sv":
    print("The vertical displacement of your projectile will be: " + str(round(vertical_displacement(), 3)) + "m")
