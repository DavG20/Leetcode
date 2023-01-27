class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        
        
        
        for i in range(len(strs[0])):
            col_char=[]
            for j in range(len(strs)):
                col_char.append(strs[j][i])
            if col_char!=sorted(col_char):
            
                count+=1
        return count
                
                
