# 给你一个整数数组 nums 和一个整数 k 。
# 每一步操作中，你需要从数组中选出和为 k 的两个整数，并将它们移出数组。
# 返回你可以对数组执行的最大操作数。
# 示例 ：
# 输入：nums = [1,2,3,4], k = 5
# 输出：2
# 解释：开始时 nums = [1,2,3,4]：
# - 移出 1 和 4 ，之后 nums = [2,3]
# - 移出 2 和 3 ，之后 nums = []
# 不再有和为 5 的数对，因此最多执行 2 次操作。
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        operation_count = 0

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == k:
                operation_count += 1
                left += 1
                right -= 1
            elif current_sum < k:
                left += 1
            else:
                right -= 1

        return operation_count
