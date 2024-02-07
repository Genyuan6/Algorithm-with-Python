# 在一个大小为 n 且 n 为 偶数 的链表中，对于 0 <= i <= (n / 2) - 1 的 i ，第 i 个节点（下标从 0 开始）的孪生节点为第 (n-1-i) 个节点 。
# 比方说，n = 4 那么节点 0 是节点 3 的孪生节点，节点 1 是节点 2 的孪生节点。这是长度为 n = 4 的链表中所有的孪生节点。
# 孪生和 定义为一个节点和它孪生节点两者值之和。
# 给你一个长度为偶数的链表的头节点 head ，请你返回链表的 最大孪生和 。
# 示例：
# 输入：head = [5,4,2,1]
# 输出：6
# 解释：
# 节点 0 和节点 1 分别是节点 3 和 2 的孪生节点。孪生和都为 6 。
# 链表中没有其他孪生节点。
# 所以，链表的最大孪生和是 6 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        value= []
        cureent = head
        while cureent:
            value.append(cureent.val)
            cureent = cureent.next
        max_sum = 0
        for i in range(len(value) // 2):
            twin_sum = value[i] + value[-1-i] #n-1-i 和-1-i是等同的，都是从列表末尾同一位置访问元素
            max_sum = max(max_sum, twin_sum)
        return max_sum
