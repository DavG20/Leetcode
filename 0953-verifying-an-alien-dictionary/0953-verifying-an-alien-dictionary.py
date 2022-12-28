class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #lets use enumerate to get order's index
        
        order_index={}
        
        for i,char in enumerate(order):
            order_index[char]=i
        
        #then compare words using bruteforce  approach
        
        for i in range(1,len(words)):
            wordA,wordB=words[i-1],words[i]
            for j in range(len(wordA)):
                if j==len(wordB): return False
                charA=wordA[j]
                charB=wordB[j]
                charA_index=order_index[charA]
                charB_index=order_index[charB]
                if charA_index<charB_index: break
                if charA_index>charB_index: return False
        return True
            
            
            