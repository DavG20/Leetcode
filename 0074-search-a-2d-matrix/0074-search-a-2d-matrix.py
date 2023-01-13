class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
                
        for i in range(len(matrix)):
            isTargetExist=self.BinarySearch(target,matrix[i])
            if isTargetExist:
                return True
        return False
    
    
    def BinarySearch(self,target,nums):
        start=0 
        end=len(nums)-1
        
        while start<=end:
            mid=(start+end)//2 
            if nums[mid] > target:
                end=mid-1
            elif nums[mid]==target:
                return True
            else:
                start=mid+1
        return False
        