class Solution:
    def minPartitions(self, n: str) -> int:
        # return int(max(n))
        #Aryan
        for d in "987654321":
            if d in n:
                return int(d)