class Solution:
    def average(self, salary: List[int]) -> float:
        max_=salary[0]
        
        sum_=0
        min_=salary[0]
        len_avg=len(salary) -2
        
        for num in salary:
            sum_+=num
            if num >max_:
                max_=num
            if num<min_:
                min_=num
        sum_-=(min_)
        sum_-=max_
        return sum_/len_avg
            