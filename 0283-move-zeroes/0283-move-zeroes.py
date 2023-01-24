class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        placeholder = 0
        seeker = 0
        while seeker < len(nums):
            if nums[seeker] != 0:
                nums[placeholder],nums[seeker]=nums[seeker],nums[placeholder]
                placeholder +=1
            seeker+=1 
#         if  len(nums)==1:
#             return nums
        
#         left = 0
        
#         seeker = 1
        
#         while seeker<len(nums) and left<seeker:
#             if nums[left]==0 and nums[seeker]!=0:
#                 nums[left],nums[seeker]=nums[seeker],nums[left]
#                 left += 1
#                 seeker += 1
                
#             elif nums[left] == 0 and nums[seeker] == 0:
#                 seeker += 1
                
#             else:
#                 left   += 1
#                 seeker += 1
        
                
                
                
            