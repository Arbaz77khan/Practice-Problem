
class Node:

    def __init__(self,value):
        self.data = value
        self.next = None

class Solution:

    def __init__(self):
        self.top = None

        self.brackets = {'(':')', '{':'}', '[':']'}

    def push(self, value):

        new_node = Node(value)

        new_node.next = self.top
        self.top = new_node

    def pop(self):

        if self.top:
            self.top = self.top.next
        
    def isValid(self, s):

        if ((s == None) or (len(s)%2 != 0)):
            return False
        
        for i in s:
            if i in self.brackets.keys():
                self.push(i)
            elif i in self.brackets.values():
                if not self.top or self.brackets[self.top.data] != i:
                    return False
                self.pop()
            else:
                return False
            
        return not self.top

S = Solution()
print(S.isValid('{}}{')) 