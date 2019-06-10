'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空
nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


        length = (len(nums1)+len(nums2))
        i = (length-1)//2
        x =  1 if length%2 else 2
        res = []
        for j in range(i+x):
            if ( not nums2 )or (nums1<=nums2 and bool(nums1)):
                res.append(nums1.pop(0))
            elif( not nums1 )or (nums1>nums2 and bool(nums2)):
                res.append(nums2.pop(0))

        ans= float(sum(res[i:i+x])/x)

        return(ans)
