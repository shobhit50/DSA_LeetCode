class Solution(object):
    def maxArea(self, height):
        res = 0
        left  = 0
        right = len(height) - 1

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            res = max(res, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        print(res)
         
            

            
        

      


height =[4,3,2,1,4]
Solution().maxArea(height)