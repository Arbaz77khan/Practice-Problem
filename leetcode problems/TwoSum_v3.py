class Solution:
    def twoSum(self, nums, target):
        my_dict = {}
        for index, item in enumerate(nums):
            complement = target - item
            if complement in my_dict:
                return [my_dict[complement], index]
            my_dict[item] = index
        return False
    
obj = Solution()
l = [2,7,0,1]
t = 2
print(obj.twoSum(l, t))
