class Solution:
    def maximumWealth(self, accounts):
        result = []
        sum = 0
        for i in range(0,len(accounts)):
            for number in accounts[i]:
                sum+=number
            result.append(sum)
            sum = 0
        main_result = max(result)
        return main_result        