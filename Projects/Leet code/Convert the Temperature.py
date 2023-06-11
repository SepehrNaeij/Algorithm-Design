class Solution:
    def convertTemperature(self, celsius):
        result = []
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.8 + 32.00
        result.append(Kelvin)
        result.append(Fahrenheit)
        return result