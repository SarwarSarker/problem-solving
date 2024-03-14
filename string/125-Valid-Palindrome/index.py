class Solution1:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''
        for i in s:
            if i.isalnum():
                new_string += i.lower()

        return new_string == new_string[::-1]



class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l< r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True