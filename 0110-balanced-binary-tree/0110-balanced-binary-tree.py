# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        
        def valid(node):
            if not node:
                return [True, 0]
            
            left, right = valid(node.left), valid(node.right)

            balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]
        return valid(root)[0]

        