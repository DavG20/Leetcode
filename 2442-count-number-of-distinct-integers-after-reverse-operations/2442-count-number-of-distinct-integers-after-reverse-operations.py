class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        len_nums =  len(nums)
        
        
        
        for i in range(len_nums):
            
            nums.append(int(str(nums[i])[::-1]))
            
        return len(set(nums))
            
            
        