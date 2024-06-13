class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        stringList = []
        score = 0

        for i in s:
            stringList.append(i)
        
        # Calculation
        for i in range(0, len(stringList)-1):
            # Take the absolute value of the ASCII versions of the current letter and subtract the next letter
            score += abs(ord(stringList[i]) - ord(stringList[i+1]))
        return score

# print(Solution.scoreOfString(None, "hello"))