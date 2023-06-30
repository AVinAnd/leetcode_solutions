"""
Given a string s, return the longest palindromic substring in s.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrom = ''
        for i in range(len(s)):
            palindrom = max(
                palindrom,
                palindrom_check(s, i, i),
                palindrom_check(s, i, i+1),
                key=len
            )
        return palindrom

def palindrom_check(string, left, right):
    while left >= 0 and right < len(string) and string[left] == string[right]:
        left -= 1
        right += 1
    return string[left + 1:right]
