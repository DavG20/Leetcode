class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        check_char=Counter(words[0])
        
        duplicate_char=[]
        
        len_words=len(words)
        
        for i in range(1,len_words):
            curr_word_count=Counter()
            
            for letter in words[i]:
                if letter in check_char and  check_char[letter]>0:
                    curr_word_count[letter]=curr_word_count.get(letter,0)+1
                check_char[letter]-=1
            check_char=curr_word_count
                    
                
                
        return check_char.elements()
                
        
        
                
        