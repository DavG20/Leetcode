class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        inbound = lambda x , y : 0 <= x < len(matrix) and 0 <= y < len(matrix[0])
        
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        
        zeros_pos = []
        
        
        for i in range(len(matrix)):
            
            for j in range(len(matrix[0])):
                
                if matrix[i][j] == 0:
                    
                    zeros_pos.append([i,j])
        print(zeros_pos)            
        for zero in zeros_pos:
            
            for dx , dy in directions:
                
                curr_x , curr_y = zero
                
                while inbound(curr_x,curr_y):
                    
                    matrix[curr_x][curr_y]=0
                    curr_x += dx
                    curr_y += dy
                    
        return matrix
                    
                
                
            
                
                
                    
                    