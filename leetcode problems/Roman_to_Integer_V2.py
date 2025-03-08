class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {"V": 5, "I": 1, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        integer = 0
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                integer += symbol[s[i]]
                i += 1
            elif (
                symbol[s[i]] == symbol["I"]
                or symbol[s[i]] == symbol["X"]
                or symbol[s[i]] == symbol["C"]
            ) and (symbol[s[i]] < symbol[s[i + 1]]):
                integer += symbol[s[i + 1]] - symbol[s[i]]
                i += 2
            else:
                integer += symbol[s[i]]
                i += 1
        return integer
    
obj = Solution()
roman = 'LXVIII'

print(obj.romanToInt(roman))