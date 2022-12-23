class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        #time complexty is NlogN
        nums.sort()
        
        #we know the max value will be at the left side
        left=len(nums)-1
        right=left-2
        
        while right>=0:
            
            if nums[left]<nums[right]+nums[right+1]:
                return nums[left]+nums[right+1]+nums[right]
            left-=1
            right-=1
        return 0
        