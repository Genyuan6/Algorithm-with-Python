class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
      #一旦 slow和fast不相等，说明 slow至少遇到了一个0
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                # Swap elements at slow and fast if they are not the same
                if slow != fast:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return nums
