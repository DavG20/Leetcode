class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        
        word1_pointer = 0 
        
        word2_pointer = 0 
        
        combined_word  =   ""
        
        while word1_pointer < len(word1) and word2_pointer < len(word2):
            
            if word1[word1_pointer:] >= word2[word2_pointer:] :
                
                combined_word += word1[word1_pointer]
                
                word1_pointer += 1
            else:
                combined_word += word2[word2_pointer]
                
                word2_pointer += 1
        while word1_pointer < len(word1):
            
            combined_word += word1[word1_pointer] 
            
            word1_pointer  += 1
        while word2_pointer < len(word2):
            
            combined_word +=word2[word2_pointer]
            
            word2_pointer += 1
            
        return combined_word
            
                
                
            
        
        