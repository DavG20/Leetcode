class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        len_grid=len(grid)
        
        #get row element from column
        column_to_row=[[] for _ in range(len_grid)]
        
        
        
        for i in range(len_grid):
            
            for j in range(len_grid):
                column_to_row[i].append(grid[j][i])
                
        count=0 
        for i in range(len_grid):
            for j in range(len_grid):
                if grid[i]==column_to_row[j]:
                    count+=1
                    #break
        return count
                    