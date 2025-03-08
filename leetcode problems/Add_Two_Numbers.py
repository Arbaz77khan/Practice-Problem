class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Solution:
    def __init__(self):
        self.head = None
        self.n = 0

    def listToLinkedlist(self, myList):
        myList = myList[::-1]
        for i in myList:
            newnode = Node(i)
            newnode.next = self.head
            self.head = newnode
            self.n = self.n + 1
        return self.head

    def addTwoNumbers(self, l1, l2):
        ll1 = self.listToLinkedlist(l1)
        ll2 = self.listToLinkedlist(l2)
        ll3 = Node(0)
        curr1 = ll1
        curr2 = ll2
        carry = 0
        dummy = Node(0)
        current = dummy

        while curr1 or curr2 or carry:
            val1 = curr1.item if curr1 else 0
            val2 = curr2.item if curr2 else 0

            total = val1 + val2 + carry
            carry, digit = divmod(total, 10)

            current.next = Node(digit)
            current = current.next

            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next

        return dummy.next
    
obj = Solution()

result = obj.addTwoNumbers([5,4,3,2,1], [3,2,1])

print(type(result))
            
