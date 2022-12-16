class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        maxSum=0
        for i in range(row-2):
            for j in range(col-2):
                tempsum=0
                for k in range(j,j+3):
                    tempsum+=grid[i][k]
                    tempsum+=grid[i+2][k]
                tempsum+=grid[i+1][j+1]
                maxSum=max(maxSum,tempsum)
        return maxSum
                