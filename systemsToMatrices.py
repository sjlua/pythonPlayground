def convert(listCoefficients: list, listEquals: list):
    """
    Transforms the coefficients into matrix form.
    """
    matrixRepresentation = []
    letters = ["x", "y", "z"]

    for i in range(0, len(listCoefficients)):
        for j in range(0,len(listCoefficients[i])):
            matrixRepresentation.append(listCoefficients[i][j])

        print(f"{matrixRepresentation}[{letters[i]}] = [{listEquals[i]}]")
        matrixRepresentation.clear()

if __name__ == "__main__":
    """
    Equations
    1x + 2y + 3z = 4
    5x + 6y + 7z = 8

    To use this, change the values in the argument below. To add another equation,
    simply add another list in the first list (listCoefficients) and add it's result 
    as the third element in the listEquals list.
    """

    convert([[1,2,3], [5,6,7]], [4,8])