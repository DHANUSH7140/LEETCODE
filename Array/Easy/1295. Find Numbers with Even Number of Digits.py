class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for num in nums if (int(math.log10(abs(num))) + 1) % 2 == 0)
