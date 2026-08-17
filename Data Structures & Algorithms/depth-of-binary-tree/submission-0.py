# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        depth = 0
        stack = deque([(1,root)])

        while stack:
            cur_depth , node = stack.popleft()
            depth = max(cur_depth,depth)
            if node.left:
                stack.append((cur_depth+1, node.left))
            if node.right:
                stack.append((cur_depth+1, node.right))
        return depth

        