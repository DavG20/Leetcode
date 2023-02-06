class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
        
        left = 0 
        
        right = len(skill) - 1
        
        target = skill[left] + skill[right]
        
        chem_sum = 0
        
        
        
        while left < right :
            
            if skill[left] + skill[right] == target :
                
                chem_sum += skill[left] * skill[right]
                left += 1
                
                right -= 1
            else:
                return -1

        return chem_sum
        
            
                
        