class Solutnon(object):   
    def sub_string(self, strs):  
        grup = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))  #create new string with sorted charecters
                                           # print(sorted_s)
            if sorted_s in grup:           # if it is true 
                grup[sorted_s].append(s)   # add the original string to the grup                         
            else:
                grup[sorted_s] = [s]       # create new key:value
        
        print(grup.values())           # print the values of the grup
        
              
        

String1 = ["eat","tea","tan","ate","nat","bat"]
Solutnon().sub_string(String1)        