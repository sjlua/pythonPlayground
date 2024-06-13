'''
Yes, the 'in' operator exists in python, but here's an algorithmic version.
'''

# Get user input for searching
searchTerm = input("Enter an integer you want to search for in the list: ")

# Validate to ensure an input was entered.
try:
    searchTerm = float(searchTerm)
except ValueError:
    raise Exception("A number was not entered, please try again.")

# A list of numbers.
listOfNumbers = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def linearSearch(searchTerm: float) -> int:        
    '''
    This function checks search value in the list and directly compares it with the user input to find the index.

    Args:
        - searchTerm (float): The user's search term.
    
    Return
        - num (int): The index of the user's search term.
    '''
    for num in range(0,len(listOfNumbers)):
        if searchTerm == listOfNumbers[num]:
            return num

print("Your number is located at index: ", linearSearch(searchTerm))


