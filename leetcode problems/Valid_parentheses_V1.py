
class Node:

    def __init__(self,value):
        self.data = value
        self.next = None

class Solution:

    def __init__(self):
        self.top = None

    def push(self, value):

        new_node = Node(value)

        new_node.next = self.top
        self.top = new_node

    def pop(self):

        if (self.top != None):
            self.top =  self.top.next
        else:
            return False
        
    def isValid(self, s):

        if ((s == None) or (len(s)%2 != 0)):
            return False
        pushLen = 0
        popLen = 0
        for i in s:
            if (i=='{' or i=='[' or i=='('):
                self.push(i)
                pushLen = pushLen + 1
            elif(i=='}' or i==']' or i==')')and (self.top != None):
                if (self.top.data =='{' and i=='}') or (self.top.data =='[' and i==']') or (self.top.data =='(' and i==')'):
                    self.pop()
                    popLen = popLen + 1
                else:
                    return False
            else:
                    return False
        if (pushLen == popLen):    
            return True
        return False

        
    

S = Solution()
print(S.isValid('1234'))
                
        


        



