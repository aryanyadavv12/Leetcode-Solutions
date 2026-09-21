class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
        
        end = [-1] * n
        
        for i in range(n):
            c = s[i]
            if first[c] == i:
                e = last[c]
                k = i
                valid = True
                while k <= e:
                    if first[s[k]] < i:
                        valid = False
                        break
                    e = max(e, last[s[k]])
                    k += 1
                if valid:
                    end[i] = e
        
        dp = [(0, 0)] * (n + 1)
        take = [False] * n
        
        for i in range(n - 1, -1, -1):
            skip_count, skip_length = dp[i + 1]
            best_count, best_length = skip_count, skip_length
            best_take = False
            
            if end[i] != -1:
                e = end[i]
                t_count = dp[e + 1][0] + 1
                t_length = dp[e + 1][1] + (e - i + 1)
                if t_count > best_count or (t_count == best_count and t_length < best_length):
                    best_count, best_length = t_count, t_length
                    best_take = True
            
            dp[i] = (best_count, best_length)
            take[i] = best_take
        
        result = []
        i = 0
        while i < n:
            if take[i]:
                e = end[i]
                result.append(s[i:e+1])
                i = e + 1
            else:
                i += 1
        
        return result