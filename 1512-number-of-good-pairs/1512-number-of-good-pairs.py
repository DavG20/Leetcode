class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        len_num=len(nums)
        for i in range(len_num):
            for j in range(i+1,len_num):
                if nums[i]==nums[j]:
                    count+=1
        return count