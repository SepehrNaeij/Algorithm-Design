class Solution:
    def runningSum(self, nums):
        result = []
        sum = 0
        for value in nums:
            sum+=value
            result.append(sum)
        return result    
    
    