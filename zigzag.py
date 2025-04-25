"""
The following is a basic solution to CodeSignal's zigzag problem.
"""
def solution(numbers):
    sol = []
    if len(numbers) < 3:
        return 0
        
    i = 0
    while (i + 2) < len(numbers):
        if numbers[i] > numbers[i+1] and numbers[i+1] < numbers[i+2]:
            sol.append(1)
        elif numbers[i] < numbers[i+1] and numbers[i+1] > numbers[i+2]:
            sol.append(1)
        else:
            sol.append(0)
        i += 1
            
    return sol

if __name__ == "__main__":
    print(solution([1, 2, 1, 3, 4]))