# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        length = 1
        last_element = head.next
        while last_element:
            length += 1
            last_element = last_element.next
        if length - n == 0:
            return head.next
        result_head = head
        for _ in range(length - n - 1):
            head = head.next
        head.next = head.next.next
        return result_head