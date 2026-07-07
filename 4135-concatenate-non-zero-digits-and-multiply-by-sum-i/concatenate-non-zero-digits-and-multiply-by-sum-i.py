class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        
        digit_sum = 0
        
        divisor = 1
        while n // divisor >= 10:
            divisor *= 10
        
        while divisor > 0:
            digit = n // divisor
            
            n %= divisor
            
            if digit != 0:
                x = x * 10 + digit
                
                digit_sum += digit
            
            divisor //= 10
        
        return x * digit_sum