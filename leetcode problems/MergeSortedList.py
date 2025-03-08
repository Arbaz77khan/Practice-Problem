class Node:
    def __init__(self, item = 0):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, item: int):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def append(self, itemss: list):
        for i in itemss:
            self.insert(i)

    def __str__(self):
        # curr = self.head
        # result = ']'
        # while curr != None:
        #     result = result + str(curr.item) + ','
        #     curr = curr.next
        # result = result[:-1] + '['
        # return result[::-1]
        curr = self.head
        result = '['  # start with [
        while curr is not None:
            result += str(curr.item)
            if curr.next:  # if not the last node, add a comma
                result += ','
            curr = curr.next
        result += ']'  # end with ]
        return result
    
    @staticmethod
    def mergeTwoLists(list1, list2):
        curr = dummy = Node()
        while list1 and list2:
            if list1.item < list2.item:
                curr.next = list1
                list1,curr = list1.next, list1
            else:
                curr.next = list2
                list2,curr = list2.next, list2

        if list1 or list2:
            curr.next = list1 if list1 else list2

        return dummy.next

    

l1 = LinkedList()
l2 = LinkedList()

l1.append([10,8,6,4,2])
print(l1)
l2.append([9,7,5,3,1])
print(l2)
result_head = LinkedList.mergeTwoLists(l1.head, l2.head)
result_list = LinkedList()
result_list.head = result_head

print(result_list)