
class Palindrome:
    def isPalindrome(self, x):
        x = str(x)
        length = len(x)
        for i in range (0, int(length/2)):
            if (x[i] != x[(length-i)-1]):
                return False
        return True

object = Palindrome()
num1 = object.isPalindrome(5005)
print(num1)