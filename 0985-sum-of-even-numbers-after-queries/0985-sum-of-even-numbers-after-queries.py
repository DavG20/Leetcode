class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum=0
        for num in nums:
            if num%2==0:
                even_sum+=num     
        result=[]
        for i in range(len(nums)):
            if nums[queries[i][1]]%2==0:
                even_sum-=nums[queries[i][1]]
            nums[queries[i][1]]=nums[queries[i][1]]+queries[i][0]
            if nums[queries[i][1]]%2==0:
                even_sum+=nums[queries[i][1]]
                result.append(even_sum)
            else:
                result.append(even_sum)
        return result