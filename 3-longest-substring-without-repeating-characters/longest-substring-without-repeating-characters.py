class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0

        for i in range(n):
          temp = ""
          for j in range(i, n):
            if s[j] in temp:  
                break
            else:
                temp += s[j]
                max_len = max(max_len, len(temp))

        return max_len