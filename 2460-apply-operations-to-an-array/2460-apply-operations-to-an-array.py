class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        len_nums=len(nums)
        
        
        
        
        
        for i in range(len_nums-1):
            
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
                prev_zero_index=i+1
        temp=-1   
        
        # for i in range(len_nums):
        #     for j in range(i+1,len_nums):
        #         if nums[i]==0 and nums[j]!=0:
        #             nums[i],nums[j]=nums[j],nums[i]
        #             break
        
        answer=[]
        count_zero=0
        
        for num in nums:
            if num==0:
                count_zero+=1
            else:
                answer.append(num)
        for _ in range(count_zero):
            answer.append(0)
                
                
                
        return(answer)