# Valid Anagram
#
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Example 1:
#          Input: s = "anagram", t = "nagaram"
#          Output: true
# Example 2:
#          Input: s = "rat", t = "car"
#          Output: false
#----------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t):
            my_string =list(t)
            my_sting2 =list(s)
            my_string.sort()
            my_sting2.sort()
            if my_string == my_sting2 :
                return True 
        return False
#     Boot force Aproche ------------>
    # if len(s) == len(t):
    #         my_string =list(t)
    #         for ch in s:
    #             if ch in my_string:
    #                 my_string.remove(ch)
    #         if len(my_string) == 0:
    #             return True
    #     return False

s = "anagram"
result = Solution().isAnagram(s, "nagaram")
print(result)                 
            
       
    
        
         
        