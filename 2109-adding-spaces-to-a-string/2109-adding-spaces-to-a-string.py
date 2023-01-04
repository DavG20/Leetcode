class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        answer=""
        
        
        answer=s[:spaces[0]]
                
        len_spaces=1
        
        while len_spaces<len(spaces):
            answer+=" " +s[spaces[len_spaces-1]:spaces[len_spaces]]
            len_spaces+=1
            
        answer+=" "+s[spaces[len_spaces-1]:]
        
        return(answer)