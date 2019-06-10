'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        dict = {}
        j = 0

        res = 0
        for i in range(len(s)):
            if s[i] in dict:
                j = max(dict[s[i]],j)

            res = max(res, i-j+1)
            ans = s[i:j]
            dict[s[i]] = i+1
        return ans
