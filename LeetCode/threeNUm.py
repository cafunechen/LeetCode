#coding: utf-8
'''
给定一个包含 n 个整数的数组 nums，判断 nums 中
是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
def threeSum(nums):
    length = len(nums)
    nums.sort()
    target = 0
    res = []
    for i in range(length):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = length - 1
        while left < right:

            temp = nums[i] + nums[left] + nums[right]
            if temp == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1

            elif temp < target:
                left += 1
            else:
                right -= 1


    return res
print(threeSum([0,0,0,0]))
