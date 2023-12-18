#Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
#          Input: nums = [2,7,11,15], target = 9
#          Output: [0,1]
#          Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#          Input: nums = [3,2,4], target = 6
#          Output: [1,2]

class Solution(object):
    def twoSum(self, nums, target):
        tgt = target
        num2 = nums.copy()  #--> list(nums)  //use this for copy list       
        num2.sort()
        start = 0
        end = len(nums)-1
        while start <end :
            summ = num2[start]+num2[end]
            if summ == tgt:
                return [nums.index(num2[start]), nums.index(num2[end])]
                # return [start, end]
            if summ> tgt :
                end -= 1
            else:
                start +=1
        



        #boot force aproche             
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
             
        
          








tg = 6
ls = [3,2,4]
print(Solution().twoSum(ls, tg))
