class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        map = {}
        sum = 0

        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1

        for i,val in map.items():
            if val == 1:
                sum += i
        return sum

