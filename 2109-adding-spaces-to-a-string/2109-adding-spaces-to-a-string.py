class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        
        modified_string=[]
        
        len_word=len(s)
        
        #change space to set for the purpose of time complexity
        space_set=set(spaces)
        
        for i in range(len_word):
            if i in space_set:
                modified_string.append(" ")
            modified_string.append(s[i])
        return "".join(modified_string)
        
#         answer=[]
        
        
#         answer.append(s[:spaces[0]])
                
#         index=1
        
#         while index<len(spaces):
#             answer.append(s[spaces[index-1]:spaces[index]])
#             index+=1
            
#         answer.append(s[spaces[index-1]:])
        
#         string_with_space=" ".join(answer)
#         return string_with_space