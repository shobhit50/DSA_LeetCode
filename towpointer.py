class Solution(object):

    def tow_sum(self, nums, target,i):
        tgt = target
        num2 = nums.copy()
        print(num2)
        start = 0
        end = len(nums)-1
        while start <end :
            summ = num2[start]+num2[end]
            data= summ + target
            if data == 0:
                return [target,num2[start],num2[end]]
            if summ> tgt :
                end -= 1
            else:
                start +=1
        return None



    def threeSum(self, nums):
        nums.sort()
        result = []
        for num in range(len(nums)):
            new_num= nums[num+1:] 
            data= self.tow_sum(new_num, nums[num],num)
            if data is not None:
                result.append(data)
        unique_result = []
        for res in result:
            if res not in unique_result:
                unique_result.append(res)
        print(unique_result)
                    


        
nums = [-2,0,1,1,2]
Solution().threeSum(nums)