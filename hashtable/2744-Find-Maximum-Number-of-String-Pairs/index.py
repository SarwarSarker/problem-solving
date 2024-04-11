class Solution1:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        
        sum = 0
        for i in range(len(words)):
            for j in range(i):
                if words[i] == words[j][::-1]:
                    sum +=1 
        return sum
      

# using hashmap
class Solution2:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        
        map = {}

        for word in words:
            if word in map:
                map[word] +=1
            else:
                map[word] =1

        sum = 0
        for word in map.keys():
            rev_word = word[::-1]
            if rev_word in map and word != rev_word:
                sum += 1
        sum //= 2  
        return sum