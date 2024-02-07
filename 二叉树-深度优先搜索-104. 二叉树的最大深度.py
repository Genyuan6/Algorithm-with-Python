# 给定一个二叉树 root ，返回其最大深度。

# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
# 示例：
# 输入：root = [3,9,20,null,null,15,7]
# 输出：3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is  None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) +1
