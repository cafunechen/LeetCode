'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

'''
 def isValid(self, s: str) -> bool:
        while '{}' in s or '()'in s or '[]' in s:
            s = s.replace('{}','')
            s = s.replace('[]','')
            s = s.replace('()','')
        return s == ''

def isValid(self, s: str) -> bool:
        S=[]
        x=''
        for i in s:
            if i=='(' or i=='[' or i=='{':
                S.append(i)
            if i==')' or i==']' or i=='}':
                if S==[]:
                    return False
                x=S.pop()+i
                if x!='()' and x!='{}' and x!='[]':
                    return False
        return S==[]
