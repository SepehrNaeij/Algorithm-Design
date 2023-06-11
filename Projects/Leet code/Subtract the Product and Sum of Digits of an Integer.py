class Solution:
    def subtractProductAndSum(self, n):
        string_number = str(n)
        sum = 0
        product = 1
        for i in range(0,len(string_number)):
            sum+=int(string_number[i])
            product*=int(string_number[i])
        return product - sum 
     