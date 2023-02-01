class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            target_indx=i
            for j in range(i+1,len(nums)):
                if nums[target_indx]>nums[j]:
                    target_indx=j
            nums[i],nums[target_indx]=nums[target_indx],nums[i]
        return nums