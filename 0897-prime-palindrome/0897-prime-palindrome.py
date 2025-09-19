import math

class Solution:
    def is_prime(self, x: int) -> bool:
        if x < 2:
            return False
        if x % 2 == 0:
            return x == 2
        r = int(math.isqrt(x))
        for d in range(3, r + 1, 2):
            if x % d == 0:
                return False
        return True

    def primePalindrome(self, N: int) -> int:
        if N <= 2:
            return 2
        if N <= 3:
            return 3
        if N <= 5:
            return 5
        if N <= 7:
            return 7
        if N <= 11:
            return 11

        length = len(str(N))
        start_len = length if length % 2 == 1 else length + 1

        for L in range(start_len, 12, 2):
            half_len = (L + 1) // 2
            start = 10**(half_len - 1)
            end = 10**half_len
            for left in range(start, end):
                s = str(left)
                pal = int(s + s[-2::-1])
                if pal >= N and self.is_prime(pal):
                    return pal
        return -1
