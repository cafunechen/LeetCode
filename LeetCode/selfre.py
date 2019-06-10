'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串'''
class Solution:
    def isMatch(self, s: str, pattern: str) -> bool:
        # write code here
        if not pattern:
            if not s:
                return True
            else:
                return False
        if len(pattern) > 1 and pattern[1] == '*':
            if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
                return self.isMatch(s[1:], pattern) or self.isMatch(s, pattern[2:])
            else:
                return self.isMatch(s, pattern[2:])
        elif len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
            return self.isMatch(s[1:], pattern[1:])
        else:
            return False
