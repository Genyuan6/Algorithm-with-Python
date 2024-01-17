class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0]*length

        # Calculate left products
        left_products = [1]*length
        for i in range(1, length):
            left_products[i] = left_products[i-1] * nums[i-1]

        # Calculate right products and the final answer
        right_product = 1
        for i in range(length-1, -1, -1):
            answer[i] = left_products[i] * right_product
            right_product *= nums[i]

        return answer
