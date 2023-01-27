class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        answer=0
        for i in range(1,n+1):
            answer=(answer+k)%i
        return answer+1
    
        