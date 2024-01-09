class stack():
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_last(self):
        return self.items[-1]
    def get_stack(self):
        return self.items
    def is_empty(self):
        return self.items == []



class Solution(object):
    def isValid(self, s):
        newStack = stack()
        is_valid = True
        index = 0
        if len(s) == 1:
            is_valid = False

        while  index < len(s) and is_valid :
            if s[index] in "{([":
                newStack.push(s[index])
            else:
                if newStack.is_empty():
                    is_valid = False
                elif s[index] == ")":
                    if "(" == newStack.is_last():
                        newStack.pop()
                    else:
                        is_valid = False
                elif s[index] == "}":
                    if "{" == newStack.is_last():
                        newStack.pop()
                    else:
                        is_valid = False
                elif s[index] == "]":
                    if "[" == newStack.is_last():
                        newStack.pop()
                    else:
                        is_valid = False
                else:
                    is_valid = False
            index += 1
        if is_valid and not newStack.is_empty():
            is_valid = False        
        if len(s) == 1:
            is_valid = False
        print(is_valid)


s = "(("
Solution().isValid(s)