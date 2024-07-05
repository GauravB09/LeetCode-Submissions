# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        head = head.next
        curr = head
        ans = [-1, -1]
        first = -1
        minDistance = 99999999999999999
        last = -1
        index = 1
        while head.next:
            # print(prev.val, curr.val, head.next.val, first, last, minDistance, index)
            if (prev.val > curr.val and curr.val < head.next.val) or (prev.val < curr.val and curr.val > head.next.val):
                if first == -1:
                    first = index
                elif first != -1 and first != index:
                    # print("Hey", first, last, index, minDistance)
                    minDistance = min(minDistance, index - last)
                last = index
            prev = curr
            head = head.next
            curr = head
            index += 1
        # print(prev.val, curr.val, first, last)
        ans[0] = -1 if minDistance == 99999999999999999 else minDistance
        ans[1] = -1 if last == first else last - first
        return ans
    