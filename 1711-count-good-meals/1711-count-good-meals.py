class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
                      
        count_good_meal=defaultdict(int)
        answer=0
        
        for meal in deliciousness:
            # i use 22 cause the max value will be 2^20 +2^20 which is 2^21 
            for i in range(22):
                answer+=count_good_meal[2**i -meal]
            
            count_good_meal[meal]+=1
            
        return answer %(10**9 +7)