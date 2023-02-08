class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0 
        
        right = 1
        
        count = 1
        
        while left < len(nums) and right < len(nums):
            
            if nums[left] ==  nums[right] :
                right += 1
            else:
                count += 1
                
                nums[left+1],nums[right] = nums[right],nums[left+1]
                
                left += 1 
            
                right += 1
                
        return count
                