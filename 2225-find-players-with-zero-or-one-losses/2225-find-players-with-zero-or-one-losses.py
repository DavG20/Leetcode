class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans=[]
        
        winner=set()
        loser=[]
        
        for player in matches:
            loser.append(player[1])
        loser_set=set(loser)
        for player in matches:
            if player[0] not in loser_set:
                winner.add(player[0])
        
        
        count_loser=Counter(loser)
        
        losers_set_final=set()
        
        for losers in count_loser.items():
            if losers[1]==1:
                losers_set_final.add(losers[0])
        ans.append(list(winner))
        ans.append(list(losers_set_final))
        ans[1].sort()
        ans[0].sort()
        return ans
        