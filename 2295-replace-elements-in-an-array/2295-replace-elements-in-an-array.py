class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        #can't pass the time limit
        # for i in range(len(operations)):
        #     for j in range(len(nums)):
        #         if operations[i][0]==nums[j]:
        #             nums[j]=operations[i][1]
        #             break
        # return nums
        
        #get the number and index pair
        
        num_index_pair={}
        
        for index,num in enumerate(nums):
            num_index_pair[num]=index

        print(num_index_pair)
        
        for operation in operations:
            index=num_index_pair[operation[0]]
            num_index_pair.pop(operation[0])
            num_index_pair[operation[1]]=index
            nums[index]=operation[1]
        return nums
            
        