class Solution:
    def shuffle(self, nums,n):
        result = []
        length = 0
        for num in nums:
            length+=1
        mid = length // 2
        for i in range(0,mid):
            result.append(nums[i])
            result.append(nums[i+mid])
        return result        