#Accepted
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x=False
        nums.sort()
        for i in range(0,len(nums)-1):
            if(nums[i]==nums[i+1]):
                x=True
                break
        return x
            
# Time Complexity issue            
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        i=0;j=1
        x=False
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if(nums[i]==nums[j]):
                    x=True
                    break
            if(x==True):
                break
        return x             
