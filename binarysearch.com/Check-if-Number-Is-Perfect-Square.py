class Solution:
    def solve(self, n):
        if n == 1:
            return True
        low_pointer, high_pointer = 0, n / 2
        while low_pointer <= high_pointer:
            mid = (low_pointer + high_pointer) // 2
            if mid * mid == n:
                return True
            elif mid * mid < n:
                low_pointer = mid + 1
            elif mid * mid > n:
                high_pointer = mid - 1
        return False


s = Solution()
print(s.solve(16))
