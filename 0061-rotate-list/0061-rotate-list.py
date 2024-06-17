# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        head_copy = head
        length = 0
        while head_copy:
            length += 1
            head_copy = head_copy.next
        if length == 0:
            return head
        prev = None
        head_copy = head
        for _ in range(length - (k%length)):
            prev = head
            head = head.next
        # print(head, prev, head_copy)
        prev.next = None
        # print(head, head_copy)
        if not head:
            return head_copy
        result_head = head
        while head.next:
            head = head.next
        head.next = head_copy
        return result_head
