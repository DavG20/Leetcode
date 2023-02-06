class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        #get the right most index
        
        right_index = {char:i for i , char in enumerate(s)}
        
        
        left = 0 
        
        right = 0
        
        answer = []
        
        for i , char in enumerate(s):
            
            right = max(right, right_index[char])
            
            if i == right :
                
                answer.append(right - left + 1)
                left = i+1
        return answer
                
                