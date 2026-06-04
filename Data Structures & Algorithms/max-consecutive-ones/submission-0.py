class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        best = 0
        for num in nums:
            if num == 1:
                current += 1
            else:
                current = 0

            if current > best:
                best = current
        return best
                
