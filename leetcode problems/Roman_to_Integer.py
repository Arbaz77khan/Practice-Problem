class Solution(object):
    def romanToInt(self, s):
        token = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        output = 0
        for i in range(len(s)):
            if (i< len(s)-1) and (token[s[i]] < token[s[i+1]]):
                output -= token[s[i]]
            else:
                output += token[s[i]]
        return output        

object = Solution()

print(object.romanToInt("LXVIII"))
