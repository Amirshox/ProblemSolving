class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        max_str = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    if len(s[i:j]) > max_len:
                        max_len = len(s[i:j])
                        max_str = s[i:j]
        return max_str


s = Solution()
print(s.longestPalindrome('cbabadcbbabbcbabaabccbabc'))
