'''
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

'''
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        i = 1
        while i<=len(nums)-1:
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i +=1

        return len(nums)
