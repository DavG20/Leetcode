class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        max_ = -1
        
        mod_arr = []
        
        for i in range(len(arr)-1,-1,-1):
            
            mod_arr.insert(0,max_)
            
            if arr[i] > max_:
                
                max_=arr[i]
        return mod_arr
            
        