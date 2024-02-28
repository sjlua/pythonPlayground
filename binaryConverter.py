''' Algorithm for Decimal to Binary conversion
Logic: https://www.wikihow.com/Convert-from-Decimal-to-Binary
'''
# Asks for an integer.
decimal = int(input("Input an integer: "))

# Stores the decimal before it gets manipulated, so it can be printed at the end.
originalDecimal = decimal

# Binary representation, if 0 is the remainder result, then it will be reversed at the end = 1.
remainder = str(decimal % 2)   

# Loop will run until the quotient (aka. decimal // 2) equals 0 or less.
while decimal // 2 > 0:
    # Returns the quotient and stores it to find the next binary number, next loop.
    decimal = decimal // 2
    # This concatenates all the remainders in reverse binary form
    remainder += str(decimal % 2)    

# This reverses the remainders/binary so that they are in order. Eg. 4 = 001 becomes 4 = 100.
binary = remainder[::-1]

# Displays the final binary form.
print("Original decimal:", originalDecimal)
print("Binary:", binary)