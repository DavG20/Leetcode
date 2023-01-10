class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        #first lets get the sum of col and reo
        
        row_sum_one=[0 for _ in range(len(grid))]
        
        row_sum_zero=[0 for _ in range(len(grid))]
        
        
        
        col_sum_one=[0 for _ in range(len(grid[0]))]
        
        col_sum_zero=[0 for _ in range(len(grid[0]))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    row_sum_zero[i]+=1
                    col_sum_zero[j]+=1
                    
                else:
                    row_sum_one[i]+=1
                    col_sum_one[j]+=1
        diff_mat=[[] for _ in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                values=(row_sum_one[i]+col_sum_one[j])-(row_sum_zero[i]+col_sum_zero[j])
                diff_mat[i].append(values)
        
        return(diff_mat)