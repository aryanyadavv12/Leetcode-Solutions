class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        curr = 0
        for i in range(n):
            curr += i * nums[i]
        
        res = curr
        for k in range(1, n):
            curr = curr + total - n * nums[n - k]
            res = max(res, curr)
        return res