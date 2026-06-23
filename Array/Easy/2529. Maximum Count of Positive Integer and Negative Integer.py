class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        c = 0
        i = 0
        while i < len(nums):
            if nums[i] < 0:
                c+=1
            i+=1
        
        return max(len(nums)-i, c)
