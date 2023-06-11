class Solution(object):
    def defangIPaddr(self, address):
        result = []
        for text in address:
            if text == '.':
                result.append("[.]")
            else:
                result.append(text)
        return "".join(result)