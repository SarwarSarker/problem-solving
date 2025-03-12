# 2529. Maximum Count of Positive Integer and Negative Integer

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos=0
        neg=0
        for num in nums:
            if num < 0 :
                neg +=1
            elif num > 0 :
                pos += 1
        return  max(pos,neg)

# class Solution:
#     def maximumCount(self, nums: List[int]) -> int:
#         lo = 0
#         hi = len(nums)-1
#         pos = 0
#         neg = 0
        
#         while lo <= hi:
#             mid = ( lo + hi ) // 2
            
#             if nums[mid] < 0:
#                 neg += mid - lo + 1
#                 lo = mid + 1
#             elif nums[mid] > 0:
#                 pos += hi - mid + 1
#                 hi = mid - 1
#             else:
#                 hi = mid - 1

#         return  max(pos,neg)
        