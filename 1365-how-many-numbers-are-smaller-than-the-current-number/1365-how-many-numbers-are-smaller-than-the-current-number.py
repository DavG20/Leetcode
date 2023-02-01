class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        sorted_num = sorted(nums)
        
        index_dic = {}
        
        answer = []
        
        for i in range(len(nums)):
            
            if sorted_num[i] not in index_dic:
                
                index_dic[sorted_num[i]] = i
                
        for i in range(len(nums)):
            
            answer.append(index_dic[nums[i]])
            
        return answer
        