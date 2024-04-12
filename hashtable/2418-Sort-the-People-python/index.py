class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        map={}

        for i in range(len(heights)):
            map[heights[i]] = names[i]
        sort_map = dict(sorted(map.items(), reverse=True))
        s=list(sort_map.values()) 

        return s