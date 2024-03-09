class Solution:
    def isPalindrome(self, x: int) -> bool:
        z = str(x)
        s = z[::-1]

        if s == z :
            return True