class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        item1 = set(nums1)
        item2 = set(nums2)

        if (item1.intersection(item2)):
            return min(item1.intersection(item2))
        else: 
            return -1