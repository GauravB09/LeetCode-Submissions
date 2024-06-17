# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        length = 2
        last_element = head.next
        while last_element.next:
            length += 1
            last_element = last_element.next
        # print(length)
        last_element.next = head
        for _ in range(length - (k%length) - 1):
            head = head.next
        result_head = head.next
        head.next = None
        return result_head
