# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        index = 0
        main_arr = []
        reverse_stack = []
        while head and index < left - 1:
            index += 1
            main_arr.append(head.val)
            head = head.next
        while head and index < right:
            index += 1
            reverse_stack.append(head.val)
            head = head.next
        # print(main_arr, reverse_stack)
        if len(main_arr) > 0:
            new_node = ListNode(main_arr[0])
            result_head = new_node
            for i in range(1, len(main_arr)):
                new_node.next = ListNode(main_arr[i])
                new_node = new_node.next
            for i in range(len(reverse_stack) - 1, -1, -1):
                new_node.next = ListNode(reverse_stack[i])
                new_node = new_node.next
            new_node.next = head
            # print(result_head, new_node)
        else:
            new_node = ListNode(reverse_stack[-1])
            result_head = new_node
            for i in range(len(reverse_stack) - 2, -1, -1):
                new_node.next = ListNode(reverse_stack[i])
                new_node = new_node.next
            new_node.next = head
        return result_head