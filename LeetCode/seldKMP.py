
def prefixTable(pattern,prefix,n):
    '''

    :param pattern:比较的文字
    :param prefix: 最终返回的公共前后缀
    :param n: 字符串长度
    :return: 公共前后缀
    '''
    prefix[0] = 0
    #第一个默认的公共前后缀
    length = 0#比较的长度
    i = 1#检测的第i个字母
    while(i<n):
        #第i个字母正好等于比较的长度的字母
        if pattern[i] == pattern[length]:
            length += 1
            prefix[i] = length
            i += 1
        else:
            if length>0:
            #如果不相等
                length = prefix[length-1]
            else:
                prefix[i] = length
                i += 1
    return prefix
def movePrefixTable(prefix,n):
    for i in range(n-1,0,-1):
        prefix[i] = prefix[i-1]
    prefix[0] = -1
def kmpSearch(text,pattern):
    n = len(pattern)
    m = len(text)
    prefix = [0]*n
    prefixTable(pattern,prefix,n)
    movePrefixTable(prefix,n)
    #text[i] len(text) = m
    #pattern[j] len(pattern) = n
    i = j = 0
    while i < m:
        if j == n-1 and text[i]==pattern[j]:
            print(i-j)
            j = prefix[j]
        if text[i]==pattern[j]:
            i += 1
            j += 1
        else:
            j = prefix[j]
            if j==-1:
                i += 1
                j += 1



if __name__ == '__main__':
    pattern = 'ABABCABAA'
    text = 'ABABCABABCABAAABABCABAA'
    kmpSearch(text,pattern)
