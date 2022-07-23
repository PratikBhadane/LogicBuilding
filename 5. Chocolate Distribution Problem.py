class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        win=M-1
        min=999999999999999
        for i in range(0,len(A)-M+1):
            diff=A[win]-A[i]
            if(diff<min):
                min=diff
            win=win+1    
                    
        return min 
