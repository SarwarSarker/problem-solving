class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = set(nums1)
        n2 = set(nums2)

        ans =[0,0]
        for i in nums1:
            if i in n2:
                ans[0] += 1

        for i in nums2:
            if i in n1:
                ans[1] += 1
        return ans