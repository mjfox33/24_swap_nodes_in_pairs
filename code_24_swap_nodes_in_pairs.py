# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        sentinel = previous_node = ListNode()
        previous_node.next = head
        while previous_node.next and previous_node.next.next:
            temp = previous_node.next
            temp2 = temp.next
            previous_node.next, temp2.next, temp.next = temp2 , temp, temp2.next
            previous_node = temp
        return sentinel.next

    def swapPairs2(self, head: ListNode) -> ListNode:
        sentinel = ListNode(0, head)
        while head and head.next:
            head.val, head.next.val = head.next.val, head.val
            head = head.next.next
        return sentinel.next