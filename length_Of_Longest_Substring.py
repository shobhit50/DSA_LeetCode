class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # if len(s) == 1:
        #     return len(s)
        # data = set()
        # l = 0
        # for i in range(len(s)):
        #     if s[i] not in data :
        #         data.add(s[i])
        #         l = max(len(data),l)
        #     elif s[i] in data:
        #         data.clear()
        #         if s[i] != s[i - 1]:
        #             data.add(s[i])
        #             data.add(s[i - 1])
        #         else:
        #             data.add(s[i])

        # print(l)
        
        data = set()
        l = 0
        j = 0
        left = 0
        while j < len(s):
                if s[j] not in data :
                    data.add(s[j])
                    l = max(len(data),l)
                    j += 1
                elif s[j] in data:
                    data.remove(s[left])
                    left += 1
        print(l)







s ="anviaj"
print(Solution().lengthOfLongestSubstring(s))
