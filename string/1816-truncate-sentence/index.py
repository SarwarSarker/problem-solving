class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        string = s.split()

        if len(string) >= k:
            del string[k:]
            s1 = ' '.join(string)
            return s1