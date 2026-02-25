class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def cnt_one(n):
            count = 0
            while n:
                n &= (n - 1)
                count += 1
            return count
        stack = []
        for i in arr:
            ones = cnt_one(i)
            stack.append((ones, i))
        heapq.heapify(stack)
        res = []
        while stack:
            res.append(heapq.heappop(stack)[1])
        return res