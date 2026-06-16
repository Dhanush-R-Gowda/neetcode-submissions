class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        for i in nums:
            ans.append(i)
        for j in nums:
            ans.append(j)
        return ans