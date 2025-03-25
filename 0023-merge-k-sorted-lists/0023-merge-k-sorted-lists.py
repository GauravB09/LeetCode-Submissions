# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        for lis in lists:
            curr = lis
            if not curr:
                curr = ListNode(float('inf'))
                continue
            while curr.next != None:
                curr = curr.next
            curr.next = ListNode(float('inf'))
        n = len(lists)
        while True:
            index = 0
            min_val = float('inf')
            for i in range(n):
                if lists[i] and lists[i].val < min_val:
                    min_val = lists[i].val
                    index = i
            if min_val == float('inf'):
                return head.next
            temp = lists[index].next
            dummy.next = lists[index]
            lists[index].next = None
            lists[index] = temp
            dummy = dummy.next