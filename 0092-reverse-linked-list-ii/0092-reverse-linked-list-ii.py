# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # temp_head = head
        # index = 1
        # if not (temp_head and temp_head.next):
        #     return temp_head
        # while head and index < left:
        #     head = head.next
        #     index += 1
        # start_pos = head
        # print(start_pos)
        # new_head = None
        # temp = head
        # if not temp:
        #     return temp_head
        # new_end = temp
        # temp_node = temp.next
        # while temp and index <= right:
        #     print(temp, temp_node, new_head, index)
        #     temp.next = new_head
        #     new_head = temp
        #     temp = temp_node
        #     temp_node = temp_node.next
        #     index += 1
        #     # print(temp, temp_node, new_head)
        # temp.next = new_head
        # new_head = temp
        # temp = temp_node
        # # print(new_end, temp, temp_node, new_head)
        # start_pos.next = new_head
        # if temp:
        #     new_end.next = temp
        # return temp_head
        # index = 1
        # if left == 1:
        #     start_pos = None
        #     end_pos = None
        #     stack = []
        #     print(index, left, right)
        #     while head and index <= right:
        #         stack.append(head.val)
        #         start_pos = head
        #         head = head.next
        #         index += 1
        #     print(stack)
        #     for i in range(len(stack) - 1, -1 , -1):
        #         print(start_pos, end_pos)
        #         if not end_pos:
        #             end_pos = ListNode(stack[i])
        #         else:
        #             end_pos.next = ListNode(stack[i])
        #             end_pos = end_pos.next
        #     # print(start_pos)
        #     start_pos.next = head
        #     return start_pos
        # temp_head = head
        # if not (temp_head and temp_head.next):
        #     return temp_head
        # while head and index < left - 1:
        #     head = head.next
        #     index += 1
        # start_pos = head
        # head = head.next
        # print(start_pos)
        # stack = []
        # while head and index < right:
        #     stack.append(head.val)
        #     head = head.next
        #     index += 1
        # print(stack)
        # for i in range(len(stack) - 1, -1 , -1):
        #     start_pos.next = ListNode(stack[i])
        #     start_pos = start_pos.next
        # start_pos.next = head
        # return temp_head
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