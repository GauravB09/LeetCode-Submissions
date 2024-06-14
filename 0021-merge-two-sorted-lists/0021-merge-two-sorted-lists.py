# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        tail = None
        while list1 and list2:
            if tail is None:
                if list1.val <= list2.val:
                    head = ListNode(list1.val)
                    list1 = list1.next
                else:
                    head = ListNode(list2.val)
                    list2 = list2.next
                tail = head
            elif list1.val <= list2.val:
                tail.next = ListNode(list1.val)
                tail = tail.next
                list1 = list1.next
            else:
                tail.next = ListNode(list2.val)
                tail = tail.next
                list2 = list2.next
        while list1:
            if tail is None:
                head = ListNode(list1.val)
                tail = head
            else:
                tail.next = ListNode(list1.val)
                tail = tail.next
            list1 = list1.next
        while list2:
            if tail is None:
                head = ListNode(list2.val)
                tail = head
            else:
                tail.next = ListNode(list2.val)
                tail = tail.next
            list2 = list2.next
        return head

                

