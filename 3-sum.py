#Finoramic Data Structures: 3-sum

# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
# Return the sum of the three integers.

# Assume that there will only be one solution

# Example: 
# given array S = {-1 2 1 -4}, 
# and target = 1.


import numpy as np 
import sys
class Solution:
    def threeSumClosest(self, arr, target):
        arr.sort()
        length = len(arr) - 1
        self.min = sys.maxsize 
        self.results = None
        for i in range(length):
            j = i + 1 
            k = length
            while j < k :
                sum =  arr[i] + arr[j] + arr[k] 
                print(arr[i], arr[j], arr[k], '=', sum )
                clos =  np.abs(sum-target)
                if clos == 0:
                    return sum
                if clos < self.min:
                    self.min = clos
                    self.results = sum
                if sum <=  target:
                    j+=1
                else:
                    k-=1
        return self.results
  

sum = Solution()
S = [-1, -2, 1, -4, 8 , 2]
target = -3
print(sum.threeSumClosest(S,target))