class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_num=[]
        negative_num=[]
        
        half_num=len(nums)//2
        
        for num in nums:
            if num>0:
                positive_num.append(num)
            else:
                negative_num.append(num)
        answer=[]
        for i in range(half_num):
            answer.append(positive_num[i])
            answer.append(negative_num[i])
        return answer
            
        
        