class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        len_word=len(words)
        count=0
        for i in range(len_word):
            for j in range(i+1,len_word):
                if set(words[i])==set(words[j]):
                    count+=1
        return count
                    
            
            