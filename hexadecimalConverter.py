'''
A hexadecimal converter that receives an integer from the user via the command line, 
then prints it in a hexadecimal format. 

Update 2
- Cleaned up the code.
- Fixed logic, so now works theoretically forever, unlike before where it wouldn't work on 10,000, 100K etc.
'''

# The hexadecimal dictionary.
hexadecimalsList = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
resultHexadecimal = ""
finalResult = ""

# Asks the user for a number.
userEnteredNumber = int(input("Input an integer: "))

# If the number entered is 0, the hexadecimal is 0. 
if (userEnteredNumber == 0):
    resultHexadecimal = "0"

# This loop runs until the quotient is equal to 0.
while (userEnteredNumber != 0):
    # Concatenates the current remainder to the current hexadecimal result.
    resultHexadecimal += str(hexadecimalsList[userEnteredNumber % 16])
    # Stores the quotient for the next division.
    userEnteredNumber = userEnteredNumber // 16

# Reverses the resultHexadecimal, as hexadecimals are filled in right to left, not left to right!
finalResult = resultHexadecimal[::-1]

# Finally, the hexadecimal is displayed.
print("Hexadecimal: " + finalResult)