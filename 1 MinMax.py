class Solution:
    def findSum(self,A,N): 
        
        #code here
        if(N==1):
            min=A[0]
            max=A[0]
        if(N>1):
            if(A[0]>A[1]):
                min=A[1]
                max=A[0]
            else:
                min=A[0]
                max=A[1]
                    
            
        
        i=0
        
        
        
        for i in range(2,N):
            if(min>A[i]):
                min=A[i]
            elif(max<A[i]):
                max=A[i]
    
        return min+max
 
 
#Driver code 
t=int(input())
for _ in range(0,t):
   n=int(input())
   a=list(map(int,input().split()))
   ob=Solution()
   print(ob.findSum(a,n))
