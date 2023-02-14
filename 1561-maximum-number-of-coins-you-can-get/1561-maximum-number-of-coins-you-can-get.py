class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        #lets sort the coin since I choose the second largest
        # make sure to give for the third person the least coin possible
        piles.sort()
        
        
        
        coin_pointer = len(piles)//3
        
        max_coin = 0
        
        while coin_pointer < len(piles):
            
            max_coin +=  piles[coin_pointer]
            
            coin_pointer += 2
            
        return max_coin

            
        
        
        