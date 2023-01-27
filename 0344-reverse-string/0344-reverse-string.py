class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        len_str=len(s)
       
        
        for i in range(len_str//2):
            s[i],s[len_str-i-1]=s[len_str-1-i],s[i]