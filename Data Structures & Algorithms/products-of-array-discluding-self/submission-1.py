class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [1] * len(nums)
        left = 1
        for i in range(len(nums)):
            p[i] = left
            left *= nums[i]
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            p[i] *= right
            right *= nums[i]
        return p 