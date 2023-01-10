class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        dict_val={}
        
        #num which has the sam index sum of row and col will have the same diagonal
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i+j in dict_val:
                    dict_val[i+j].append(mat[i][j])
                else:
                    dict_val[i+j]=[mat[i][j]]
        answer=[]
        
        print(dict_val)
        for group_num in dict_val.items():
            if group_num[0]%2==0:
                [answer.append(num) for num in group_num[1][::-1]]
            else:
                [answer.append(num) for num in group_num[1]]
        return(answer)
                