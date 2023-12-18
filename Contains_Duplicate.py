# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:
#           Input: nums = [1,2,3,1]
#           Output: true
# Example 2:
#          Input: nums = [1,2,3,4]
#          Output: false
class Solution(object):
    def containsDuplicate(self, nums):
        ls = set()
        for num in nums:
            if num in ls :
                return True
            else:
                ls.add(num)
        return False
    
nu = [1, 2, 3, 4, 1]
# solution_instance = Solution()
result = Solution().containsDuplicate(nu)
print(result)