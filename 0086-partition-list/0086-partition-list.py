# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        result_node = None
        result_head = result_node
        temp_node = None
        temp_head = temp_node
        while head:
            if head.val < x:
                if not result_node:
                    result_node = ListNode(head.val)
                    result_head = result_node
                else:
                    result_node.next = ListNode(head.val)
                    result_node.next.next = temp_head
                    result_node = result_node.next
            else:
                if not temp_node:
                    temp_node = ListNode(head.val)
                    temp_head = temp_node
                else:
                    temp_node.next = ListNode(head.val)
                    temp_node = temp_node.next
            # print(f"Head: {head}\nResult Head: {result_head}\nTemp Head: {temp_head}\nTemp Node: {temp_node}")
            head = head.next
        if not result_node:
            return temp_head
        if not result_node.next:
            result_node.next = temp_head
        return result_head


