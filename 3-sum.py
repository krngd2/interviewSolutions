#Finoramic Data Structures: 3-sum

# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
# Return the sum of the three integers.

# Assume that there will only be one solution

# Example: 
# given array S = {-1 2 1 -4}, 
# and target = 1.


import numpy as np

s =[-1, 2, 1, -4]   # given Array
target = 1          # given target
results = []        # results of sum of 3 numbers in array 

# raise exception if array length is less than 3
if len(s) < 3:
    raise Exception('Array Must be length of more than 3')

# to add 3 numbers in an array loop array 3 times
for i in range(len(s)):  
    for j in range(len(s)):
        if not s[i] == s[j]: # preventing adding self
            for k in range(len(s)):
                if not s[i] == s[k] and not s[j] == s[k]  :     # preventing adding to self
                    print((s[i],s[j], s[k]),'=',s[i] + s[j] + s[k] )
                    addedResult = s[i] + s[j] + s[k]            
                    if addedResult not in results:              # preventing duplicate entries
                        results.append(addedResult)             # adding to the results array


print(results) 

# getting the nearest value to target from the results array using numpy
# loop through the results and get absolute values when subtracted from the target 
# and append to another array to preserve its index
absoluteValues= [] 
absoluteValues.append([np.abs(i - target) for i in results])  

# get the index of the minimum value of absoluteValues array 
# and get the value of the same index from results array
print(results[absoluteValues.index(min(absoluteValues))])       
# result is 2 