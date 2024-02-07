给你一个二进制数组 nums ，你需要从中删掉一个元素。
请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。
如果不存在这样的子数组，请返回 0 。
提示 1：
输入：nums = [1,1,0,1]
输出：3
解释：删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        max_length = 0
        zero_count = 0

        for right in range(len(nums)):
            # 如果右指针指向的元素是0，增加zero_count
            if nums[right] == 0:
                zero_count += 1

            # 当窗口内有超过一个0时，移动左指针
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # 更新最大长度
            max_length = max(max_length, right - left + 1)

        # 返回最大长度减1（因为我们可以删除一个0）
        return max_length - 1
