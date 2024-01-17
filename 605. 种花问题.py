# 假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
# 给你一个整数数组 flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false 
# 问题的关键在于遍历当前地块的左右两边是否满足要求，要注意i == 0是表示当前地块是第一块，i == length -1 是表示当前地块是最后一块
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0  # Number of flowers that can be planted
        length = len(flowerbed)

        for i in range(length):
            # Check if current plot is empty and the adjacent plots are also empty or non-existent
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == length-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1  # Plant a flower
                count += 1  # Increment the count

            if count >= n:
                return True  # Early exit if we have planted enough flowers

        return False  # Return false if not enough spaces to plant flowers
