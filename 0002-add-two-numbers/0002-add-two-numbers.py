# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        tail = None
        extra = False
        while l1 and l2:
            a = l1.val
            b = l2.val
            new_val = a + b + int(extra)
            extra = new_val >= 10
            if not tail:
                tail = ListNode(new_val%10)
                head = tail
            else:
                new_node = ListNode(new_val%10)
                tail.next = new_node
                tail = tail.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            new_val = l1.val + int(extra)
            extra = new_val >= 10
            if not tail:
                tail = ListNode(new_val%10)
                head = tail
            else:
                new_node = ListNode(new_val%10)
                tail.next = new_node
                tail = tail.next
            l1 = l1.next
        while l2:
            new_val = l2.val + int(extra)
            extra = new_val >= 10
            if not tail:
                tail = ListNode(new_val%10)
                head = tail
            else:
                new_node = ListNode(new_val%10)
                tail.next = new_node
                tail = tail.next
            l2 = l2.next
        if extra:
            if not tail:
                tail = ListNode(1)
                head = tail
            else:
                new_node = ListNode(1)
                tail.next = new_node
                tail = tail.next
        return head
