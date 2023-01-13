class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer=[0 for _ in range(len(boxes))]
        
        for i in range(len(boxes)):
            
            for j in range(i+1,len(boxes)):
                if boxes[i]=="1" and boxes[j]=="1":
                    answer[i]+=j-i
                    answer[j]+=j-i
                elif boxes[i]=="1" and boxes[j]=="0":
                    answer[j]+=j-i
                
                elif boxes[i]=="0" and boxes[j]=="1":
                    
                    answer[i]+=j-i
                    
        return answer
                    