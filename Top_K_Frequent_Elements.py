class Solutnon(object):
    def top_k_frequent(self, nums, k):
        my_dict={}
        for n in nums:
            if n in my_dict:
                my_dict[n] += 1
            else:
                my_dict[n] = 1
        print(my_dict)
        # num_short = sorted( my_dict.items())
        sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
        print(sorted_dict)
        top_k_elements = [key for key, value in sorted_dict[:k]]
        return top_k_elements  
    
    
num = [1,1,1,2,2,3]
k =2
Solutnon().top_k_frequent(num, k)