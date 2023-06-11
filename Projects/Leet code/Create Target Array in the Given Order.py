class Solution:
    def createTargetArray(self, nums, index):
        result = []
        for i in range(0,len(nums)):
            result.insert(index[i],nums[i])
        return result    