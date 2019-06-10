'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = end =0
        for i in range(len(s)):
            len1 = self.centerexpand(s,i,i)
            len2 = self.centerexpand(s,i,i+1)
            maxlen = max(len1,len2)
            if maxlen > end -start +1:
                start = i - (maxlen-1)//2
                end = i + maxlen//2
        return s[start:end+1]
    def centerexpand(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l = l-1
            r = r+1
        return r -l -1
