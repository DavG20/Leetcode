class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        reshape_mat = [[] for _ in range(r)]
        
        original_elm = [mat[i][j] for i in range(len(mat)) for j in range(len(mat[0]))]
        
        count=0
        
        if r==len(mat) and c==len(mat[0]):
            
            return mat
        # if r==1 or c==1:
        #     return [original_elm]
        if r * c == len(mat) * len(mat[0]):
            
            for i in range(r):
            
                for j in range(c):
                    
                    reshape_mat[i].append(original_elm[count])
                    count+=1
            return reshape_mat
        else:
            return mat
        