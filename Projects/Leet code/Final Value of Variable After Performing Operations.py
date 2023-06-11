class Solution:
    def finalValueAfterOperations(self, operations):
        count = 0
        for text in operations:
            if text[0] == "-" or text[2] == "-":
                count-=1
            elif text[0] == "+" or text[2] == "+":
                count+=1   
        return count        
