给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。
请返回层内元素之和 最大 的那几层（可能只有一层）的层号，并返回其中 最小 的那个。
示例 1：
输入：root = [1,7,0,7,-8,null,null]
输出：2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [root]
        maxSum = float("-inf") #二叉树也有可能存在负数的值，所以为了确保选择无穷小
        maxLevel = 1
        level = 1
        while queue:
            levelSum = sum(node.val for node in queue)
            if levelSum > maxSum:
                maxSum = levelSum
                maxLevel = level
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return maxLevel
