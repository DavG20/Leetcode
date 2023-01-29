class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        inbound = lambda x , y : 0 <= x < len(matrix) and 0 <= y < len(matrix[0])
        
        direction = [1,1]
        
        for i in range(len(matrix)):
            dx , dy = direction
            
            for j in range(len(matrix[0])):
                curr_x = i 
                curr_y = j
                ans=set()
                while inbound(curr_x,curr_y):
                    print(curr_x,curr_y)
                    ans.add(matrix[curr_x][curr_y])
                    curr_x += dx
                    curr_y += dy
                if len(ans)>1:
                    return False
        return True
                    
                
                
                    
                    
            
            
        