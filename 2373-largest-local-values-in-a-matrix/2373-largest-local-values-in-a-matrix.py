class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        
        max_local=[[] for _ in range(len(grid[0])-2)]
        
        
        intial_win=[]
        
        for i in range(3):
            intial_win.append(grid[i][:3])
        #print(intial_win)
        
        for i in range(len(grid)-2):
            
            for k in range(len(grid)-2):
                max_=-float('inf')
                for j in range(3):
                    int_win=grid[i+j][k:3+k]
                    
                    if max_<max(int_win):
                        max_=max(int_win)
                max_local[i].append(max_)
        return max_local
                        
                
                
            
                
            