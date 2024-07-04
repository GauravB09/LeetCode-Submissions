# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sum = 0
        temp_head = ListNode(-1)
        temp_start = temp_head
        while head.next:
            head = head.next
            if head.val == 0:
                temp_head.next = ListNode(sum)
                temp_head = temp_head.next
                sum = 0
            else:
                sum += head.val
        return temp_start.next