class Solution:
    def addTwoNumbers(self, l1, l2):
        l1 = l1[::-1]
        l2 = l2[::-1]

        if len(l1) > len(l2):
            l2.extend([0] * (len(l1) - len(l2)))
        elif len(l1) < len(l2):
            l1.extend([0] * (len(l2) - len(l1)))
        print(l1,l2)
        l3 = [i + j for i, j in zip(l1, l2)]
        print(l3)
        carry = 0

        for i in range(len(l3)):
            l3[i] += carry
            carry = l3[i] // 10
            l3[i] %= 10

        while carry:
            l3.append(carry % 10)
            carry //= 10

        return l3[::-1]

obj = Solution()
result = obj.addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9])
print(result)
