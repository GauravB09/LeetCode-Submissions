# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        count = 0
        value = head.val
        result_head = None
        new_node = None
        while head:
            if head.val == value:
                count += 1
            else:
                if count == 1:
                    if not new_node:
                        new_node = ListNode(value)
                        result_head = new_node
                    else:
                        new_node.next = ListNode(value)
                        new_node = new_node.next
                value = head.val
                count = 1
            head = head.next
        if count == 1:
            if not new_node:
                new_node = ListNode(value)
                result_head = new_node
            else:
                new_node.next = ListNode(value)
                new_node = new_node.next
        return result_head
        