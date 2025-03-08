class Solution:
    def removeElement(self, nums, val):
        nums.remove(val)
        print(nums)
        return len(nums)
    
S = Solution()
result = S.removeElement([0,1,2,2,3,0,4,2], 2)

print(result)