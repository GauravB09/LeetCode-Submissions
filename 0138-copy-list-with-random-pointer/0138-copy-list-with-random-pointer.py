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
        if not head:
            return None
        dic1 = {}
        dic2 = {}
        dic3 = {}
        result_node = result_head = Node(0)
        curr = head
        arr = []
        index = 0
        while curr:
            dic3[(curr, curr.val)] = index
            index += 1
            curr = curr.next
        curr = head
        index = 0
        while curr:
            result_node.next = Node(curr.val)
            result_node = result_node.next
            dic2[index] = (result_node, result_node.val)
            if curr.random:
                dic1[index] = dic3[(curr.random, curr.random.val)]
            curr = curr.next
            index += 1
        result_node = result_head.next
        index = 0
        # print(dic1)
        # print(dic2)
        # print(dic3)
        while result_node:
            if index in dic1:
                result_node.random = dic2[dic1[index]][0]
            result_node = result_node.next
            index += 1
        return result_head.next
        