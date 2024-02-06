# 给你一个链表的头节点 head 。删除 链表的 中间节点 ，并返回修改后的链表的头节点 head 。
# 长度为 n 链表的中间节点是从头数起第 ⌊n / 2⌋ 个节点（下标从 0 开始），其中 ⌊x⌋ 表示小于或等于 x 的最大整数。
# 对于 n = 1、2、3、4 和 5 的情况，中间节点的下标分别是 0、1、1、2 和 2 。
# 示例
# 输入：head = [1,3,4,7,1,2,6]
# 输出：[1,3,4,1,2,6]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 特殊情况处理：链表为空或只有一个节点
        if not head or not head.next:
            return None

        # 计算链表长度
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # 定位到中间节点的前一个节点
        mid = length // 2
        current = head #需要重新更新一下current，因为之前的current已经在遍历链表时到了链表的尾端了
        for _ in range(mid-1): #一定要使用mid-1而不是mid，这样current才会停留在mid的前一个节点上
            current = current.next

        # 删除中间节点
        current.next = current.next.next

        return head
