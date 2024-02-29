'''
A hexadecimal converter that receives an integer from the user via the command line, 
then prints it in a hexadecimal format.
'''

# The hexadecimal dictionary.
hexadecimalsList = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
resultHexadecimal = ""
finalResult = ""

# Asks the user for a number.
userEnteredNumber = int(input("Input an integer: "))

# A loop that runs until the remainder = 0, meaning the full hexadecimal has been found.
if userEnteredNumber % 16 != 0:
	# The fast method uses the remainder to find part of the hexadecimal and appends from left to right.
	while userEnteredNumber % 16 != 0:
		# Takes the remainder, uses it as an index number and finds the corresponding hexadecimal,
		# then appending it to the final resultHexadecimal.
		resultHexadecimal = str(resultHexadecimal) + str(hexadecimalsList[userEnteredNumber % 16])
		# Takes the quotient and stores it in the variable to recursively divide by 16 until remainder = 0.
		userEnteredNumber = userEnteredNumber // 16

# As multiples of 16 do not have a remainder (eg. 32/6 = 2), the following condition must exist.
elif userEnteredNumber % 16 == 0:
	resultHexadecimal = "0"
	# Adds the result to the hexadecimal.
	resultHexadecimal = str(resultHexadecimal) + str(userEnteredNumber // 16)

# Reverses the resultHexadecimal, as hexadecimals are filled in right to left, not left to right! ty google
finalResult = resultHexadecimal[::-1]

# Finally, the hexadecimal is displayed.
print("Hexadecimal: " + finalResult)