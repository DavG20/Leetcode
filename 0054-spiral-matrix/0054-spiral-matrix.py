class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        answer = []
        
        while matrix:
            
            answer+=matrix.pop(0)
            
            if matrix and matrix[0]:
                for array in matrix:
                    answer.append(array.pop())
            if matrix:
                #reverse the array last andd add
                answer+=matrix.pop()[::-1]
                
            if matrix and matrix[0]:
                
                for arr in matrix[::-1]:
                    answer.append(arr.pop(0))
        return(answer)
        
        
                