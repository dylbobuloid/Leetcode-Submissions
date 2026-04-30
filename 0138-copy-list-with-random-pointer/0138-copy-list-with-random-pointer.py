"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        listToCopy = {None:None}
        cur = head

        while cur:
            copy = Node(cur.val)
            listToCopy[cur] = copy
            cur = cur.next

        
        cur = head

        while cur:
            copy = listToCopy[cur]
            copy.next = listToCopy[cur.next]
            copy.random = listToCopy[cur.random]
            cur = cur.next
        
        return listToCopy[head]
        