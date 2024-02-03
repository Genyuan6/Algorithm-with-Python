# 给你一个整数数组 nums ，请计算数组的 中心下标 。
# 数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。
# 如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。
# 如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1 。
# 示例 1：
# 输入：nums = [1, 7, 3, 6, 5, 6]
# 输出：3
# 解释：
# 中心下标是 3 。
# 左侧数之和 sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11 ，
# 右侧数之和 sum = nums[4] + nums[5] = 5 + 6 = 11 ，二者相等。
# 示例 2：
# 输入：nums = [1, 2, 3]
# 输出：-1
# 解释：
# 数组中不存在满足此条件的中心下标。
# 对于下标 0（元素是 2）：
# 左侧元素之和 = 0（因为下标 0 左侧没有元素）
# 右侧元素之和 = 1 + (-1) = 0
# 这里左侧和右侧的和都是 0，因此符合条件。
# 示例 3：
# 输入：nums = [2, 1, -1]
# 输出：0
# 解释：
# 中心下标是 0 。
# 左侧数之和 sum = 0 ，（下标 0 左侧不存在元素），
# 右侧数之和 sum = nums[1] + nums[2] = 1 + -1 = 0 。

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == total_sum - left_sum -num:
                return i
            left_sum += num
        return -1
