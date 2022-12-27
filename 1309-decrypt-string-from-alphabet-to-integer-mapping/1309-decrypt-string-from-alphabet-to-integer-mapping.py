class Solution:
    def freqAlphabets(self, s: str) -> str:
        stack=[]
        ans=""
        letters="abcdefghijklmnopqrstuvwxyz"
        print(len(letters))
        for chrs in s:
            stack.append(chrs)
        while stack:
            if stack[-1]=="#":
                _=stack.pop()
                v1=stack.pop()
                v2=stack.pop()
                index=int(v2+v1)-1
                ans=letters[index]+ans
                
            else:
                
                indexs=int(stack.pop())-1
                ans=letters[indexs]+ans
        return ans
                
                