
###### Kadane’s Algorithm  ########
Initialize:
    max_so_far = INT_MIN
    max_ending_here = 0

Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
  (c) if(max_ending_here < 0)
            max_ending_here = 0
return max_so_far
######################



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_so_far=-99999999999999
        max_ending_here=0
        for i in range(0,len(nums)):
            max_ending_here=max_ending_here + nums[i]
            if(max_ending_here>max_so_far):
                max_so_far=max_ending_here

            if(max_ending_here<0):
                max_ending_here=0

        return max_so_far
