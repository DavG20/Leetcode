class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_val=0
        
        for char in s:
            char_val^=ord(char)
        for char in t:
            char_val^=ord(char)
        return chr(char_val)