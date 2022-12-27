class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""
        
        len_word1=len(word1)
        len_word2=len(word2)
        min_len=min(len_word2,len_word1)
        i=0
        while i<(min_len):
            ans+=word1[i]
            ans+=word2[i]
            i+=1
        # if i<len_word1:
        ans+=word1[i:]
        # if i<len_word2:
        ans+=word2[i:]
        return ans
    
            
        
        
        
            