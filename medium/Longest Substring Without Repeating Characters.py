"""
Given a string s, find the length of the longest substring without repeating characters.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left, right = 0, 0
        length = 1
        symbols = {s[left]: 0}
        while right != len(s) - 1:
            right += 1
            if s[right] in symbols:
                index = symbols[s[right]]
                while left <= index:
                    if s[left] in symbols:
                        del symbols[s[left]]
                    left += 1

            symbols[s[right]] = right
            new_length = right - left + 1
            if new_length > length:
                length = new_length

        return length
