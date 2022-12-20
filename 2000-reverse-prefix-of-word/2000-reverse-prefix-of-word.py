class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            ans=""
            for i in range(len(word)):
                ans+=word[i]
                if word[i]==ch:
                    return ans[::-1]+word[i+1:]
                
        else:
            return word