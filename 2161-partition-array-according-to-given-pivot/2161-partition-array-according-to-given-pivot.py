class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_pivot=[]
        greater_pivot=[]
        equal_piv=[]
        for num in nums:
            if num<pivot:
                less_pivot.append(num)
            elif num>pivot:
                greater_pivot.append(num)
            else:
                equal_piv.append(num)
        nums[:]=less_pivot[:]+equal_piv[:]+greater_pivot[:]
        return nums