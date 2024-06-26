"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # if not head:
        #     return None
        # dic1 = {}
        # dic2 = {}
        # dic3 = {}
        # result_node = result_head = Node(0)
        # curr = head
        # arr = []
        # index = 0
        # while curr:
        #     dic3[(curr, curr.val)] = index
        #     index += 1
        #     curr = curr.next
        # curr = head
        # index = 0
        # while curr:
        #     result_node.next = Node(curr.val)
        #     result_node = result_node.next
        #     dic2[index] = (result_node, result_node.val)
        #     if curr.random:
        #         dic1[index] = dic3[(curr.random, curr.random.val)]
        #     curr = curr.next
        #     index += 1
        # result_node = result_head.next
        # index = 0
        # # print(dic1)
        # # print(dic2)
        # # print(dic3)
        # while result_node:
        #     if index in dic1:
        #         result_node.random = dic2[dic1[index]][0]
        #     result_node = result_node.next
        #     index += 1
        # return result_head.next

        if not head:
            return None
        old_to_new = {}
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next
        return old_to_new[head]
        
        # if not head:
        #     return None
        
        # curr = head
        # while curr:
        #     new_node = Node(curr.val, curr.next)
        #     curr.next = new_node
        #     curr = new_node.next
            
        # curr = head
        # while curr:
        #     if curr.random:
        #         curr.next.random = curr.random.next
        #     curr = curr.next.next
        
        # old_head = head
        # new_head = head.next
        # curr_old = old_head
        # curr_new = new_head
        
        # while curr_old:
        #     curr_old.next = curr_old.next.next
        #     curr_new.next = curr_new.next.next if curr_new.next else None
        #     curr_old = curr_old.next
        #     curr_new = curr_new.next
            
        # return new_head