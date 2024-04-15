class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}

        for i in s:
            if i not in map:
                map[i] =1
            else:
                map[i] +=1
                
        for i,v in enumerate(s):
            if map[v] == 1:
                return i
        return -1