'''
Test cases for gcdivisor
- b > a done
- a > b done
- a = b done
- a%b = 0 done
- a%b =/0 done
- b = 0 done
- a = 0 done
'''

# User enters a (+ve integer)
a = int(input("Please enter a value for a: "))

# User enters b (+ve integer)
b = int(input("Please enter a value for b: "))

# If b > a, this variable will be temporarily used. Otherwise it won't be used.
tempA = a

# The final gcd.
gcdivisor = 0

# Division theorem variables, a = qb+r
q = a//b
r = a%b

# Displays the initial question
print(str(a) + " = " + str(q) + "(" + str(b) + ")" + " + " + str(r))

# The euclidean formula
def euclideanLoop():
    # Allows the modification of a, b, q, r from within the local function.
    global a,b,q,r
    q = a//b # Returns q in DT           
    r = a%b # Returns r in DT    
    # Stops an extra loop from running if r == 0. Prints final equation.
    if r == 0:
        print(str(a) + " = " + str(q) + "(" + str(b) + ")" + " + " + str(r))                    
    else:        
    # Prints every line.      
        print(str(a) + " = " + str(q) + "(" + str(b) + ")" + " + " + str(r))
        a = b # Stores next testing GCD
        b = r # Stores last remainder as b                  
    
# If b is 0,  then gcdivisor is immediately a.
if b == 0:
    gcdivisor = a    

# If a is 0,  then gcdivisor is immediately b.
elif a == 0:
    # Notation will be wrong though.
    gcdivisor = b   

# Swapping variables so the original algorithm continues to work even if b > a.
elif b > a:    
    # Notation will be wrong though.
    a = b
    b = tempA

    # Ensures the correct amount of loops run based on remainder.
    if r == 0:
        euclideanLoop()
        # Assigns the final a value as the gcdivisor once the remainder is 0.
        gcdivisor = b
    elif r!= 0:
        while r != 0:
            euclideanLoop()
        # Assigns the final a value as the gcdivisor once the remainder is 0.
        gcdivisor = a

# For every other case where b is not equal to 0.
else:
    # Ensures the correct amount of loops run based on remainder.
    if r == 0:
        euclideanLoop()
        # Assigns the final a value as the gcdivisor once the remainder is 0.
        gcdivisor = b
    elif r!= 0:
        while r != 0:
            euclideanLoop()
        # Assigns the final a value as the gcdivisor once the remainder is 0.
        gcdivisor = a
        

# Displays the final result.
print("The greatest common divisor: ", gcdivisor)