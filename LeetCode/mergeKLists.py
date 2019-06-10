'''
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        amount = len(lists)
        count = 1
        while count<amount:
            for i in range(0,amount-count,count*2):
                lists[i] = self.merge2Lists(lists[i],lists[i+count])
            count *= 2
        return lists[0] if amount > 0 else lists
    def merge2Lists(self,l1,l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val<=l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next

            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next
