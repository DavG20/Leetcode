class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        #to get the largest perimeter lets sort the array first
        nums.sort() #time complexity NlogN
        
        right=len(nums)-1
        left=right-2
        
        while left>=0:
            if nums[right]<nums[left]+nums[left+1]:
                return nums[left]+nums[left+1]+nums[right]
            left-=1
            right-=1
        return 0