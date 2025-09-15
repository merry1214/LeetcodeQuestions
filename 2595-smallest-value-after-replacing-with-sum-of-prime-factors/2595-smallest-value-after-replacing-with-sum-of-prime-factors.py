class Solution:
    def smallestValue(self, n: int) -> int:
        if n <= 1:
            return n

        def sum_prime_factors(x: int) -> int:
            s = 0
           
            while x % 2 == 0:
                s += 2
                x //= 2
            
            f = 3
            
            while f * f <= x:
                while x % f == 0:
                    s += f
                    x //= f
                f += 2
            
            if x > 1:
                s += x
            return s

        while True:
            s = sum_prime_factors(n)
            if s == n:
                return n
            n = s
        