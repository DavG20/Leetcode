class Solution:
    def interpret(self, command: str) -> str:
        i=0
        ans=""
        while i <len(command):
            if command[i]=="G":
                ans+="G"
                i+=1
            elif command[i]=="(" and command[i+1]==")":
                ans+="o"
                i+=2
            else:
                ans+="al"
                i+=4
        return ans
                
                
            