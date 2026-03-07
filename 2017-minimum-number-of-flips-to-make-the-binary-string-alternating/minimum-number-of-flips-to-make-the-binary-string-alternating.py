class Solution:
    #Aryan
    def minFlips(self, s):
        n = len(s)
        s = s + s
        
        p1 = ''.join('0' if i % 2 == 0 else '1' for i in range(2 * n))
        p2 = ''.join('1' if i % 2 == 0 else '0' for i in range(2 * n))
        
        f1 = f2 = 0
        min_flips = float('inf')
        
        i = 0
        for j in range(2 * n):
            if s[j] != p1[j]:
                f1 += 1
            if s[j] != p2[j]:
                f2 += 1
            
            if j - i + 1 > n:
                if s[i] != p1[i]:
                    f1 -= 1
                if s[i] != p2[i]:
                    f2 -= 1
                i += 1
            
            if j - i + 1 == n:
                min_flips = min(min_flips, min(f1, f2))
        
        return min_flips