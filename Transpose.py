class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n=len(matrix[0])
        m=len(matrix)
        ans=[[0]*m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                ans[j][i]=matrix[i][j]
        return ans
