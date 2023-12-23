class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """ 
        new = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    new[i] *= nums[j]
        return new




num = [1,2,4,5]
print(Solution().productExceptSelf(num))