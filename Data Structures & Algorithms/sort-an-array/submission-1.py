class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        mid=(len(nums))//2
        left=self.sortArray(nums[:mid])
        right=self.sortArray(nums[mid:])
        return self.merg(left,right)

    def merg(self, left: List[int], right: List[int]) -> List[int]:
        temp=[]
        i=0
        j=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                temp.append(left[i])
                i=i+1
            else:
                temp.append(right[j])
                j=j+1
        temp.extend(left[i:])
        temp.extend(right[j:])
        return temp