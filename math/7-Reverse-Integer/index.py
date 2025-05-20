class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        string = str(x)

        if string[0] == '-':
            rev_string = '-' + string[:0:-1]
        else:
            rev_string = string[::-1]
        y = int(rev_string)

        return y if INT_MIN <= y <= INT_MAX else 0