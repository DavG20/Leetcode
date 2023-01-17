class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for i in range(len(names)):
            
            min_index=i
            
            for j in range( i + 1, len(names)):
                if heights[min_index ]< heights[j]:
                    
                    min_index=j
                    
            names[min_index],names[i]=names[i],names[min_index]
            
            heights[min_index],heights[i]=heights[i],heights[min_index]
            
        return names
                    
                    