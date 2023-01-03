class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        columnTitle=""
        
        while columnNumber>0:
            
            remainder=(columnNumber-1)%26
            
            columnNumber=(columnNumber-1)//26
            
            columnTitle=chr(remainder+65)+columnTitle
            
        return columnTitle