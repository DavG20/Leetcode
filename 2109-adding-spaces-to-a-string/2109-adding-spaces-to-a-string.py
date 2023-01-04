class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        answer=[]
        
        
        answer.append(s[:spaces[0]])
                
        index=1
        
        while index<len(spaces):
            answer.append(s[spaces[index-1]:spaces[index]])
            index+=1
            
        answer.append(s[spaces[index-1]:])
        
        string_with_space=" ".join(answer)
        return string_with_space