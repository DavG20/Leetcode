class Solution:
    def printVertically(self, s: str) -> List[str]:
        max_len_string=0
        word_list=s.split()
        
        
        #get the max len word
        for word in word_list:
            if len(word)>max_len_string:
                max_len_string=len(word)
        
        len_list=len(word_list)
        
        answer=[]
        
        for i in range(max_len_string):
            vertical_word=""
            for j in range(len_list):
                if i<len(word_list[j]):
                    vertical_word+=word_list[j][i:i+1]
                else:
                    vertical_word+=" "
            answer.append(vertical_word.rstrip())
        
        return answer
        
        