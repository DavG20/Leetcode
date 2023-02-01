class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        answer = []
        
        num = self.mergeSort(nums)
        
        print(num)
        
        for i in range(len(num)):
            if target == num[i]:
                answer.append(i)
                
        return answer
        
        
        
    def mergeSort(self,nums):
        
        if len(nums)>1:
            r = len(nums)//2
        
            L = nums[:r]

            R = nums [r:]



            self.mergeSort(L)

            self.mergeSort(R)

            k = 0

            i = 0

            j = 0

            while i < len(L) and j < len(R):

                if L[i] < R[j]:
                    nums[k] = L[i]
                    i+=1
                else:
                    nums[k] = R[j]
                    j+=1
                k+=1

            while i < len(L):
                nums[k] = L[i]

                i += 1
                k += 1
            while j < len(R):
                nums[k] = R[j]
                j += 1

                k += 1
            return nums
        else:
            return nums
            
        
        
        
        