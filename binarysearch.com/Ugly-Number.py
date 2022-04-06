class Solution:
    def solve(self, n):
        involving_prime_number = [2, 3, 5]
        yes_no = False

        if n == 0:
            yes_no = False
        else:
            for factor in involving_prime_number:
                while n % factor == 0:
                    n = n / factor

        return n == 1
