'''
Algorithm for GCD
Khan Academy: https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
- This prints out the actual steps so you can see how it works if you were to do it on paper.
'''

# User enters a (+ve integer)
a = int(input("Please enter a value for a: "))

# User enters b (+ve integer)
b = int(input("Please enter a value for b: "))

def gcdivisor(a, b):
    # If either of the numbers are 0, the other one is immediately the gcdivisor.
    if b == 0:
        return a
    elif a == 0:
        return b
    
    # Calculates initial remainder
    remainder = a%b
    
    # If b is already the greatest divisor of a,
    if remainder == 0:
        print(str(a) + " = " + str(a//b) + "(" + str(b) + ")" + " + " + str(a%b))
        return b

    # Continues until reminader = 0, as this means the current value of a is the gcdivisor.
    while (remainder) != 0:
        quotient = a//b
        remainder = a%b
        print(str(a) + " = " + str(quotient) + "(" + str(b) + ")" + " + " + str(remainder))
        a = b # Stores the next potential GCD.
        b = remainder
    
    # The a value after the while loop is the previous b value, which would be the gcd.
    return a

# Displays the final result.
print("The greatest common divisor: ", gcdivisor(a,b))