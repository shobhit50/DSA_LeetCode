class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = []
        right = []
        max_left = height[0]
        max_right = height[-1]
        total = 0
        for i in range(len(height)):
            data2 = max(max_left , height[i])
            max_left= data2
            left.append(data2)
            data = max(max_right , height[len(height)-1 - i])
            max_right= data
            right.append(data)

         
        for i in range(len(height)):
            water = min(left[i],right[len(right) - 1 - i])
            total += water - height[i]
            print (total)
            
        
        # print(total)
            
        

height = [4,2,0,6,3,2,5]
Solution().trap(height)