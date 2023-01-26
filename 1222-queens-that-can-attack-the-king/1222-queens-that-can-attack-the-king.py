class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1),
                        (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        queen_pos = set([tuple(queen) for queen in queens])
        ans = []
        inbound = lambda x, y : 0 <= x < 8 and 0 <= y < 8
        
        for dx, dy in directions:
            curr_x, curr_y = king
            
            while inbound(curr_x, curr_y) and \
                (curr_x, curr_y) not in queen_pos:
                curr_x, curr_y = curr_x + dx, curr_y + dy
                
            if (curr_x, curr_y) in queen_pos:
                ans.append([curr_x, curr_y])
        
        return ans