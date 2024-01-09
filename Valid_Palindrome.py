class Solution(object):
    # def isPalindrome(self, s):
    #     new_s = ""
    #     for char in s:
    #         if char.isalnum():
    #             new_s += char.lower() 
    #     print(new_s,'fisrt')
    #     print(new_s[::-1],'second')
    #     return True
        
           
    #     # char.isalnum()


    def checkPalindrome(self, s):
        new = dict()
        new2 = ''
        print(s)
        for i in range(65, 123):
            new[chr(i)] = []  # Use characters as keys

        for i in range(len(s)):
            if s[i] in new:
                new2 += s[i].lower()  # Concatenate s[i] to new2
        
        print(new2[::-1])
        return  new2 == new2[::-1],
                
            

   



s ="A man, a plan, a canal: Panama"
print(Solution().checkPalindrome(s))