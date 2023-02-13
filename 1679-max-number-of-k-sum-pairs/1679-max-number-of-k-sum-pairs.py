class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        #lets sort the array
        #then pick from the two end and check if k == to the sum of the two
        
        
        nums.sort()
        
        left = 0 
        
        right = len(nums) - 1
        
        count = 0
        
        while  left < right:
            
            if nums[left] + nums[right] == k :
                count += 1
                left += 1 
                right -= 1
                
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        return count