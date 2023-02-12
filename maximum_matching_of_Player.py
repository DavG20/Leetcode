class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        count=0
        players.sort()
        trainers.sort()
        j=0
        for num in players:
            while j<len(trainers):
                if num<=trainers[j]:
                    count+=1
                    j+=1
                    break
                else:
                    j+=1
        return count
            
        
