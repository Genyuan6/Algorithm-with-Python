# 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，请你返回一个长度为 2 的列表 answer ，其中：
# answer[0] 是 nums1 中所有 不 存在于 nums2 中的 不同 整数组成的列表。
# answer[1] 是 nums2 中所有 不 存在于 nums1 中的 不同 整数组成的列表。
# 注意：列表中的整数可以按 任意 顺序返回。
# 示例 1：
# 输入：nums1 = [1,2,3], nums2 = [2,4,6]
# 输出：[[1,3],[4,6]]
# 解释：
# 对于 nums1 ，nums1[1] = 2 出现在 nums2 中下标 0 处，然而 nums1[0] = 1 和 nums1[2] = 3 没有出现在 nums2 中。因此，answer[0] = [1,3]。
# 对于 nums2 ，nums2[0] = 2 出现在 nums1 中下标 1 处，然而 nums2[1] = 4 和 nums2[2] = 6 没有出现在 nums2 中。因此，answer[1] = [4,6]。
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hash_nums1 = {num: True for num in nums1}
        has_nums2 = {num: True for num in nums2}
        diff1 = [num for num in nums1 if num not in has_nums2]
        diff2 = [num for num in nums2 if num not in hash_nums1]
        return [list(set(diff1)), list(set(diff2))]
