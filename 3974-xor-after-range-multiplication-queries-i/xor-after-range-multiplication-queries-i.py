class Solution(object):
    #Aryan
    def xorAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        
        for q in queries:
            idx=q[0]
            ri=q[1]
            ki=q[2]
            vi=q[3]
            while idx<=ri:
                nums[idx]=(nums[idx]*vi)%(10**9+7)
                idx+=ki
        r = 0
        for num in nums:
            r ^=num
        return r

        