class Solution:
    def removeDuplicates(self, nums):
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j, nums

S = Solution()
k,j = S.removeDuplicates([1,1,2])
print(k, j)