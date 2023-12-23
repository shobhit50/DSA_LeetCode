class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 :
            return 0
        if len(nums) == 1:
            return 1

        my_set = set()
        count = 0
        check = False
        nums.sort()
        for i in range(len(nums)-1):
            if (nums[i] +1 == nums[i+1] or nums[i] == nums[i+1]):
                my_set.add(nums[i])  
                my_set.add(nums[i + 1])              
                if check:
                    my_set.clear()
                    my_set.add(nums[i])
                    check = False
            else:
                check = True
            count = max(count, len(my_set))
            
        return count
        

num = [100,4,200,1,3,2]
print(Solution().longestConsecutive(num))