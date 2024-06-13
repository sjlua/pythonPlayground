class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        ans = []

        kelvin = celsius + 273.15
        farenheit = celsius*(1.80) + 32

        ans.extend([kelvin,farenheit])

        return ans
    
# print(Solution.convertTemperature(None, 36.50))