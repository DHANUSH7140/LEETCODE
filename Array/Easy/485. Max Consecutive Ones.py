class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m, c = 0, 0
        for i in nums:
            if i:
                c+=1
            else:
                m = max(c, m)
                c = 0
        return max(c, m)
