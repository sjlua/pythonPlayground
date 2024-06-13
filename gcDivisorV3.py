'''
Recursion with gcd
- This does not print out the actual steps.
'''

def rec_gcd(a: int, b: int) -> int:
    '''
    Computes the greatest common divisor of two numbers recursively with Euclid's algo.

    Args:
        - a (int)
        - b (int)
    Return:
        - gcd (int)
    '''
    # (Base case) If b is already 0, a is the gcd
    if b == 0:
        return a
    # Recurse towards base case
    else:
        # Assign b to a, and the remainder of a%b as b
        return rec_gcd(b, a%b)

print("The greatest common divisor of:", rec_gcd(106,6))