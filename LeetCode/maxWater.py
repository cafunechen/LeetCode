'''
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，
使得它们与 x 轴共同构成的容器可以容纳最多的水。
输入 [1,8,6,2,5,4,8,3,7]
输出 49
这道题最粗暴的方法当然是O(n^2)，当然对于medium难度的题目来说，显然不能这么做
这道题要解决的问题是，找寻最大的一组(i,j)，使得Area最大

Area = Max(min(height[i], height[j]) * (j-i)) {其中0 <= i < j < height,size()}
这里用到了动态规划，基本的表达式: area = min(height[i], height[j]) * (j - i) 使用两个指针，
值小的指针向内移动，这样就减小了搜索空间 因为面积取决于指针的距离与值小的值乘积，
如果值大的值向内移动，距离一定减小，而求面积的另外一个乘数一定小于等于值小的值，
因此面积一定减小，而我们要求最大的面积，因此值大的指针不动，而值小的指针向内移动遍历
'''
height = [1,8,6,2,5,4,8,3,7]
def maxWater(height):
    left = 0
    right = len(height)-1
    maxArea = 0
    while left<right:
        distence = (right-left)
        if height[left]<height[right]:
            minh = height[left]
            left+=1
        else:
            minh = height[right]
            right-=1
        Area =  distence*minh
        maxArea = max(maxArea,Area)
    return maxArea

height = [1,8,6,2,5,4,8,3,7]
print(maxWater(height))
