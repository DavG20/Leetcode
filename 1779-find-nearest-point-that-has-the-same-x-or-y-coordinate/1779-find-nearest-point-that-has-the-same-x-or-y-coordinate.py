class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_=sys.maxsize
        index=-1
        for i,point in enumerate(points):
            if point[0]==x or point[1]==y:
                distance=abs((point[0]-x)+(point[1]-y))
                if min_>distance:
                    min_=distance
                    index=i
        return index
            