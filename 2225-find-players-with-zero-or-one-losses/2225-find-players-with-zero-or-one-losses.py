class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans=[]
        
        winner=set()
        loser=[]
        
        for player in matches:
            loser.append(player[1])
        
        #lets change loser to set it will help us not retriev 
        #every time to check if winner is in or not in loser
        #time complexity to change list to set is O(n)
        loser_set=set(loser)
        
        for player in matches:
            #in here in oprator time complexity is O(1)
            if player[0] not in loser_set:
                winner.add(player[0])
        
        #lets get the freq of loser since we want the one time losers only
        count_loser=Counter(loser)
        
        #again lets use set , it will help us not to check if loser is already in our lis or not
        losers_set_final=set()
        
        for losers in count_loser.items():
            if losers[1]==1:
                losers_set_final.add(losers[0])
        ans.append(list(winner))
        ans.append(list(losers_set_final))
        ans[1].sort()
        ans[0].sort()
        return ans
        