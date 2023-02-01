#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        target_indx=i
        for indx in range(i+1,len(arr)):
            if arr[target_indx]>arr[indx]:
                target_indx=indx
        arr[i],arr[target_indx]=arr[target_indx],arr[i]
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            self.select(arr,i)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends