class Solution(object):
    def convertTemperature(self, celsius):
        """
        This takes the Celsius temperature and converts it to Kelvin and Farenheit.

        Args:
            - Celsius (float/int): The temperature in Celsius.
        
        Return:
            - ans (list): This is a list containing the Kelvin and Farenheit temp.
        """
        # Empty list initialised
        ans = []

        # Formula for Kelvin
        kelvin = celsius + 273.15
        # Formula for Farenheit
        farenheit = celsius*(1.80) + 32

        # This appends two values to the ans list variable, Kelvin and Farenheit
        ans.extend([kelvin,farenheit])

        # Returns the converted temperatures.
        return ans 
    
# print(Solution.convertTemperature(None, 36.50))