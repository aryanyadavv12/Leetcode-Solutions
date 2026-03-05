class Solution:
    #Aryan
    def minOperations(self,s):
        val = '0'
        a = 0
        b = 0

        for c in s:
            if val != c:
                a += 1

            if val == '0':
                val = '1'
            else:
                val = '0'

        val = '1'

        for c in s:
            if val != c:
                b += 1

            if val == '0':
                val = '1'
            else:
                val = '0'

        return min(a, b)