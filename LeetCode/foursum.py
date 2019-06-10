'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        res = []
        for i in range(length-3):
            for j in range(i+1,length-2):
                left,right = j+1,length-1
                while left<right:
                    curSum = nums[i]+nums[j]+nums[left]+nums[right]
                    if curSum==target:
                        x = [nums[i],nums[j],nums[left],nums[right]]
                        if x not in res:
                            res.append(x)
                        left += 1
                        right -= 1
                    elif (curSum<target):
                        left += 1
                    else:
                        right -=1
        return res
                        
