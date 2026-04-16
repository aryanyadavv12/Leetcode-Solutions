class Solution:
    #Aryan
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        l = len(nums)
        last_index = {}
        distances = [inf] * l

        for i in range(l + (l // 2)):
            n = nums[i%l]
            if n in last_index:
                j = last_index[n]
                if i % l == j:
                    continue
                d = i - j
                distances[i%l] = min(distances[i%l], d)
                distances[j%l] = min(distances[j%l], d)
            last_index[n] = i
        
        return [-1 if (d := distances[q]) == inf else d for q in queries]