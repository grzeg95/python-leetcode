# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        depth = 0
        stack = [(root, 1)]

        # while stack is not empty
        while stack:

            node, node_depth = stack.pop()

            # if node is not None
            if node:
                stack.append((node.left, node_depth + 1))
                stack.append((node.right, node_depth + 1))
                depth = max(depth, node_depth)

        return depth
