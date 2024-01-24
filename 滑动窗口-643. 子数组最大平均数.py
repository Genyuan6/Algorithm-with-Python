# 给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。
# 请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。
# 任何误差小于 10-5 的答案都将被视为正确答案。
# 示例 1：
# 输入：nums = [1,12,-5,-6,50,3], k = 4
# 输出：12.75
# 解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k]) #切片操作，取nums前k个元素，所以取到了索引为k-1的元素
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i-k]
            max_sum = max(window_sum, max_sum)
        return max_sum / k
