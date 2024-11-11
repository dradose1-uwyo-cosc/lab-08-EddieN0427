# Your Name Here
# UWYO COSC 1010
# Submission Date
# Lab XX
# Lab Section:
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def change(input):
    if input.lstrip('-').isdigit() and '.' not in input:  
        return int(input)
    try:
        val_of_float = float(input)
        if '.' in input and input.count('.') == 1 and len(input.split('.')[1]) == 1:
            return val_of_float
        else:
            return False
    except ValueError:
        return False
print(change("1"))
print(change("1.1"))
print(change("eee"))
print(change("1.1111"))


print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope(m, b, lowX, upX):
    try:
        lowX = int(lowX)
        upX = int(upX)
    except ValueError:
        return False
    if lowX > upX:
        return False
    y_val = []
    for x in range(lowX, upX + 1):
        y = m * x + b
        y_val.append(y)
    return y_val
def the_input(prompt):
    entered = input(prompt)
    if entered.lower() == 'exit':
        return None
    return entered
while True:
    m_put = the_input("Enter the slope (m)), or 'exit' to quit: 1 ")
    if m_put is None:
        break
    b_put = the_input("Enter the intercept (b), or 'exit' to quit: 2 ")
    if b_put is None:
        break
    low_x_put = the_input("Enter the lower x bound, or 'exit' to quit: 3  ")
    if low_x_put is None:
        break
    up_x_put = the_input("Enter the upper x bound, or 'exit' to quit: exit ")
    if up_x_put is None:
        break
    try:
        m = float(m_put)  
        b = float(b_put) 
        lowX = int(low_x_put) 
        upX = int(up_x_put)  
        result = slope(m, b, lowX, upX)
        if result is False:
            print("Invalid, the bounds need to be integers and in the range.")
        else:
            print("The y values are:", result)
    except ValueError:
        print("Invalid, enter valid numbers.")


print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null


def sq_rt(x):
    if x < 0:
        return None 
    elif x == 0:
        return 0  
    else:
        maybe = x / 2
        ok = 1e-10 
        while True:
            hmm_maybe = (maybe + x / maybe) / 2
            if abs(maybe - hmm_maybe) < ok:
                return hmm_maybe
            maybe = hmm_maybe
def solve_it(a, b, c):
    under_rad = b**2 - 4 * a * c 
    sqrt_under_rad = sqrt(under_rad) 
    if sqrt_under_rad is None:
        return "No real roots"
    rt1 = (-b + sqrt_under_rad) / (2 * a)
    rt2 = (-b - sqrt_under_rad) / (2 * a)
    return rt1, rt2
def get_it(prompt):
    used = input(prompt)
    if used.lower() == 'exit':
        return None
    return used
while True:
    a_entered = get_it("Enter value for a 'exit': 1 ")
    if a_entered is None:
        break
    b_entered = get_it("Enter value for b or 'exit': 2 ")
    if b_entered is None:
        break
    c_entered = get_it("Enter value for c, or 'exit': 3 ")
    if c_entered is None:
        break
    try:
        a = float(a_entered)
        b = float(b_entered)
        c = float(c_entered)
        answer = solve_it(a, b, c)
        if (answer, tuple):
            print(f"The solutions are: x1 = {answer[0]}, x2 = {answer[1]}")
        else:
            print(answer)  
    except ValueError:
        print("Invalid, enter valid numbers.")
