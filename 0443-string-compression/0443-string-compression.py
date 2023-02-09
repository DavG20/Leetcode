class Solution:
    def compress(self, chars: List[str]) -> int:
        
        left = 0 
        
        right = 0
        
        s = ""
        
        while left < len(chars) and right < len(chars):
            
            while right<len(chars) and chars[left] == chars[right]:
                right += 1
            s += chars[left]
            if (right - left)>1:
                s += str(right-left)
            left = right
            
        for i in range(len(s)):
            chars[i] = s[i]
        return len(s)
                
                        
            
            
        
        