class Solution1:
    def checkIfPangram(self, sentence: str) -> bool:
        map = {}
        for i in sentence:
            if i in map:
                map[i] +=1
            else:
                map[i] = 1

        for l in 'abcdefghijklmnopqrstuvwxyz':
            if l not in map:
                return False
        return True



class Solution2:
    def checkIfPangram(self, sentence: str) -> bool:
        word = set()
        for i in sentence:
            word.add(i)
        
        return len(word) == 26