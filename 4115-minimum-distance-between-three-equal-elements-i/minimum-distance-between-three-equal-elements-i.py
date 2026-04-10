class Solution:
    #Aryan
    def minimumDistance(self, nums):
        from collections import defaultdict

        mp = defaultdict(list)

        for i, val in enumerate(nums):
            mp[val].append(i)

        ans = float('inf')

        for v in mp.values():
            if len(v) >= 3:
                for i in range(len(v) - 2):
                    d = 2 * (v[i + 2] - v[i])
                    ans = min(ans, d)

        return -1 if ans == float('inf') else ans