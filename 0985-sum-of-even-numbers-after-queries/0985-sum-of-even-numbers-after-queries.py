class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        pre_even_sum=0
        
        
        #get the intial even sum
        
        for num in nums:
            if num%2==0:
                pre_even_sum+=num
        
        new_nums=nums[:]
        
        answer=[]
        
        for query in queries:
            if new_nums[query[1]]%2==0:
                pre_even_sum-=new_nums[query[1]]
                modified_val=new_nums[query[1]]+query[0]
                if modified_val%2==0:
                    new_nums[query[1]]=modified_val
                    pre_even_sum+=modified_val
                    answer.append(pre_even_sum)
                else:
                    new_nums[query[1]]=modified_val
                    answer.append(pre_even_sum)
                    
            else:
                modified_val=new_nums[query[1]]+query[0]
                if modified_val%2==0:
                    new_nums[query[1]]=modified_val
                    pre_even_sum+=modified_val
                    answer.append(pre_even_sum)
                else:
                    new_nums[query[1]]=modified_val
                    answer.append(pre_even_sum)
        return answer

                
                    
            
                