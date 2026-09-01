class Solution:

    def trap(self, height: List[int]) -> int:
        tw = 0
        n = len(height)
        if n < 3:
            return 0
        max_l = [0] * n
        max_r = [0] * n
        max_l[0] = height[0]
        for i in range(1, n):
            max_l[i] = max(max_l[i - 1], height[i])
        max_r[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            max_r[i] = max(max_r[i + 1], height[i])
        for i in range(1, n - 1):
            w = min(max_l[i - 1], max_r[i + 1]) - height[i]
            if w > 0:
                tw += w
        return tw