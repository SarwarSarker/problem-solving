class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0

        for i in range(n):
            sum += nums[i]
        
        actual_sum = n*(n+1)//2
        return actual_sum -sum

# binary search
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        l,r = 0,len(nums)

        while l<r:
            mid = (l+r)//2
            if nums[mid] > mid:
                r = mid
            else:
                l = mid+1
        return l