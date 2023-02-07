class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[]
        for num in nums:
            if num not in res:
                res.append(num)
        for i in range(len(res)):
            nums[i]=res[i]
        nums=nums[:len(res)]
        return len(nums)
        