# BROKEN | DO NOT USE | BROKEN | DO NOT USE | BROKEN | DO NOT USE | BROKEN | DO NOT USE | BROKEN | DO NOT USE |

def binarySearch(sortedNumerics: list[int], value: int):
    point = round((len(sortedNumerics))/2)
    upper = len(sortedNumerics) - 1
    lower = 0
    
    print(value)
    print(point)
    print(sortedNumerics[point])

    if sortedNumerics[point] == value:
        return point
    elif value < sortedNumerics[point]:
        lower = point
    elif value > sortedNumerics[point]:
        upper = point
        
    # dividedList = sortedNumerics[lower:upper]
    # binarySearch(dividedList, value)

# A sorted array of integers.
sortedNumerics = [1,2,3,4,5,6,7]

# Takes integer from user.
value = int(input("Enter in a value that you'd like to search for: " ))

print("Your number is located at index value", binarySearch(sortedNumerics, value))
