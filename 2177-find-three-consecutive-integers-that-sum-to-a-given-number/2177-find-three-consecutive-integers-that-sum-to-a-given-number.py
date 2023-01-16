class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        middle_num=num//3
        
        if (middle_num+middle_num+1+middle_num-1)==num:
            return [middle_num-1,middle_num,middle_num+1]
        else:
            return []