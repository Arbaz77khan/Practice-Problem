class Solution:
    def addTwoNumbers(self, l1, l2):
        l1 = l1[::-1]
        l2 = l2[::-1]
        # print(l1,l2)
        if len(l1) > len(l2):
            zero = len(l1)-len(l2)
            for i in range(zero):
                l2.insert(0, 0)
            # print(l2)   
        elif len(l1) < len(l2):
            zero = len(l2)-len(l1)
            for i in range(zero):
                l1.insert(0, 0)
            # print(l1)  
        l3 = [i+j for i, j in zip(l1, l2)]
        # print(l3)
        loop = True
        while loop:
            for i in range(len(l3)):
                if l3[i] >= 10:
                    if i == 0:
                        l3.insert(0,1)
                        l3[i+1] = l3[i+1]%10
                    else:
                        l3[i-1] = l3[i-1] + 1
                        l3[i] = l3[i]%10
                    loop = True
                
            for item in l3:
                if item >= 10:
                    loop = True
                    break
                else:
                    loop = False
                    
            
        return l3[::-1]
    
obj = Solution()

result = obj.addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9])

print(result)