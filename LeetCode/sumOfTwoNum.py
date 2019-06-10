'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        str1 = ''
        str2 = ''
        while l1 or l2:
            if l1:
                str1+=str(l1.val)
                l1 = l1.next
            if l2:
                str2+=str(l2.val)
                l2 = l2.next
        n1 = int(str1[::-1])
        n2 = int(str2[::-1])
        reslist = list(str(n1+n2))
        head = p= ListNode(reslist.pop())
        while reslist:
            q = ListNode(reslist.pop())
            p.next = q
            p = q

        return head
