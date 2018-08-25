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
    def ClosestOfSum(self, arr, target):
        arr.sort()                  # sorting will return ascending clossest value while not sorting will return random
        length = len(arr) - 1       # getting the length of the array
        self.min = sys.maxsize      # reference to max value to store the lowest minimum value 
        self.result = None          # reference to result
        for i in range(length):     # Loop through array to add
            j = i + 1               
            k = length
            while j < k :           
                sum =  arr[i] + arr[j] + arr[k] # sum of items

                # print(arr[i], arr[j], arr[k], '=', sum )

                clos =  np.abs(sum-target)      # getting the absoculte closest value 

                if clos == 0:                   # if value is equal to the target 
                    return sum                  # return sum

                if clos < self.min:             # comparing the previous closest value to the present closest value 
                    self.min = clos             # if lowser store it 
                    self.result = sum           # store the sum into results

                if sum <=  target:              # if sum is less than the target increase j if not lower k 
                    j+=1
                else:
                    k-=1

        return self.result                      # return the final result
  

# Sample

# sum = Solution()
# S = [-1, -2, 1, -4]
# target = 2
# print(sum.ClosestOfSum(S,target))