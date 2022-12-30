class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_sub_url=defaultdict(int)
        answer=[]
        
        for domain in cpdomains:
            num_visit_url=domain.split()
            
            num_visited=int(num_visit_url[0])
            
            
            url_part=num_visit_url[1].split(".")
            num_url=len(url_part)-1
            
            url=url_part[num_url]
            
            for i in range(num_url,0,-1):
                count_sub_url[url]+=num_visited
                url=url_part[i-1]+"."+url
            count_sub_url[url]+=num_visited 
                
        for domain_count in count_sub_url.items():
            answer.append(str(domain_count[1])+" "+domain_count[0])
        return answer