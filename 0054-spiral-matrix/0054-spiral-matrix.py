class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        answer = []
        
        while matrix:
            
            answer+=matrix.pop(0)
            
            if matrix and matrix[0]:
                
                for array in matrix:
                    
                    answer.append(array.pop())
            
            if matrix:
                
                answer+=matrix.pop()[::-1]
                
            if matrix and matrix[0]:
                
                for array in matrix[::-1]: 
                    answer.append(array.pop(0))
        return answer