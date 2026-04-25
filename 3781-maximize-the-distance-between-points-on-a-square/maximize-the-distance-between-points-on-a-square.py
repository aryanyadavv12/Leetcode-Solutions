class Solution:
    #Aryan
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        def flatten(point: List[int]):
            x, y = point[0], point[1]
            if y == 0: return x
            if x == side: return side + y
            if y == side: return 2 * side + (side - x)
            return 3 * side + (side - y)
        
        temp = []
        for p in points:
            temp.append((flatten(p), p[0], p[1]))
        flattern_arr = sorted(temp)
        
        left = 1
        right = 2 * side
        
        def isSatisfyManhattan(threshold: int):
            n = len(flattern_arr)
            sorted_pts = [(p[1], p[2]) for p in flattern_arr]
            sorted_pts = sorted_pts + sorted_pts
            
            next_pt = [2 * n] * (2 * n)
            j = 1
            for i in range(2 * n):
                if j <= i:
                    j = i + 1
                while j < 2 * n:
                    x = sorted_pts[i][0] - sorted_pts[j][0]
                    y = sorted_pts[i][1] - sorted_pts[j][1]
                    if abs(x) + abs(y) >= threshold:
                        break
                    j += 1
                next_pt[i] = j
                
            min_diff = 2 * n + 1
            i_min = -1
            for i in range(n):
                if next_pt[i] - i < min_diff:
                    min_diff = next_pt[i] - i
                    i_min = i
                    
            if min_diff > n // k:
                return False
                
            for start_idx in range(i_min, next_pt[i_min] + 1):
                start = start_idx % n
                curr = start
                for _ in range(k):
                    curr = next_pt[curr]
                    if curr >= 2 * n:
                        break
                if curr <= start + n:
                    return True
            return False

        while left <= right:
            mid = left + (right - left) // 2
            if isSatisfyManhattan(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right