'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

'''
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        front = ListNode(0)
        #留head
        front.next,fast,slow = head,front,front
        while (n or fast):
            if n : fast,n = fast.next,n-1
            else:
                fast = fast.next
                slow = slow.next if fast else slow
        slow.next = slow.next.next
        return front.next
