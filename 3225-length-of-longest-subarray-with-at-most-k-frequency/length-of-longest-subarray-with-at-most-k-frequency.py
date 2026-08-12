class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        res = 0
        count = {}
        n = len(nums)
        for i in range(n):
            count[nums[i]] = count.get(nums[i], 0) + 1
            while count[nums[i]] > k:
                count[nums[left]] -= 1
                left += 1
            res = max(res, i - left + 1)
        return res