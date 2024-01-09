class Solution(object):
    def twoSum(self, numbers, tgt):
        start= 0
        end = len(numbers)-1
        while start<end:
            check = numbers[start] + numbers[end]
            if check == tgt:
                print(numbers[start] , numbers[start+1], 'data')
                if numbers[start] == numbers[start+1]:
                    return(numbers.index(numbers[start])+1,numbers.index(numbers[end])+2)
                else:
                    return(numbers.index(numbers[start])+1,numbers.index(numbers[end])+1)
            
            if check > tgt:
                end -= 1
            else:
                start += 1


new_list = [0,0,3,4]
tgt = 0
print(Solution().twoSum(new_list,tgt))