class Solution1 :
    def isPalindrome(self, x: int) -> bool:
        z = str(x)
        s = z[::-1]

        if s == z :
            return True

class Solution2:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        rev=0

        while(x>0):
            digit= x%10
            rev = (rev*10) + digit
            x = x//10
        if temp == rev:
            return True
