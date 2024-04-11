# BROKEN | DO NOT USE | BROKEN | DO NOT USE | BROKEN | DO NOT USE | BROKEN | DO NOT USE | BROKEN | DO NOT USE |

# A sorted array of integers.
sortedNumerics = [1,2,3,4,5,6,7]

# Takes integer from user.
value = int(input("Enter in a value that you'd like to search for: " ))

# The comparison point.
pivotPoint = int(len(sortedNumerics)/2)

# The new start and end point.
startPoint = int(0)
endPoint = int(0)

# Location of value within array, aka index.
locationOfValue = 9999

for i in range(0, len(sortedNumerics)):
    if value < sortedNumerics[pivotPoint]:
        pivotPoint = int(pivotPoint/2)
    elif value > sortedNumerics[pivotPoint]:
        pivotPoint = int((len(sortedNumerics)-pivotPoint)/2)
    elif value == sortedNumerics[pivotPoint]: #works
        locationOfValue = pivotPoint
    else:
        locationOfValue = "Number has not been found :("

# for i in range(0, len(sortedNumerics)):
#     while sortedNumerics[endPoint] > value > sortedNumerics[pivotPoint]:
#         startPoint = pivotPoint + 1        
#         endPoint = len(sortedNumerics)
#         pivotPoint = int(endPoint/2)
#     while sortedNumerics[startPoint] < value < sortedNumerics[pivotPoint]:
#         startPoint = sortedNumerics[0]      
#         endPoint = pivotPoint - 1
#         pivotPoint = int(sortedNumerics[pivotPoint])
#     if value == sortedNumerics[pivotPoint]: #works
#         locationOfValue = pivotPoint
#     else:
#         locationOfValue = "Number has not been found :("6	
print("Your number is located at index value", locationOfValue)
