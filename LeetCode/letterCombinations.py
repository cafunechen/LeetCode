'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。


'''
def a(digits):

    m = {
        '2': list('abc'),
        '3': list('def'),
        '4': list('ghi'),
        '5': list('jkl'),
        '6': list('mno'),
        '7': list('pqrs'),
        '8': list('tuv'),
        '9': list('wxyz'),
        }
    if not digits: return []
    ls1 = ['']
    for i in digits:
        ls1 = [x + y for x in ls1 for y in m[i]]
    return ls1
print(a('23'))
