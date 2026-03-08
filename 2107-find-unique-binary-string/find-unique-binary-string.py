class Solution(object):
    #Aryan
    def findDifferentBinaryString(self, nums):
        done = [int(num, 2) for num in nums]
        n = len(nums)
        for i in range(n+1):
            if not i in done:
                return format(i, '0'+str(n)+'b')